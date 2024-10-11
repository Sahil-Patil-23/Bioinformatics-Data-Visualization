import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy
import matplotlib.image as mpimg
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--outputFile','-o',default='Assignment5.png',type=str,action='store',help='output file goes here')
parser.add_argument('--sequences','-c',default='Splice_Sequences.fasta',type=str,action='store',help='input file goes here')

args = parser.parse_args()
outFile=args.outputFile
inFile=args.sequences



A = mpimg.imread('A.png')
T = mpimg.imread('T.png')
G = mpimg.imread('G.png')
C = mpimg.imread('C.png')

dict_of_seq = {}
sequence = []
with open(inFile , 'r') as file:
    for line in file:
        if line.startswith('>'):
            if sequence:
                combine_seq = ''.join(sequence)
                dict_of_seq[name] = combine_seq
                sequence = []
            name = line[1:].strip().split()[0]
        else:
            sequence.append(line.strip())
    if sequence:
        combine_seq = ''.join(sequence)
        dict_of_seq[name] = combine_seq

s3 = []
s5 = []
for name,sequence in dict_of_seq.items():
    if name.startswith('5'):
        s5.append(sequence)
    else:
        s3.append(sequence)

string3 = ''.join(s3)
string5 = ''.join(s5)

pos_list_s5 = [{'A':0 , 'T':0 , 'G':0 , 'C':0} for i in range(20)]
pos_list_s3 = [{'A':0 , 'T':0 , 'G':0 , 'C':0} for i in range(20)]


en_s5 = (1/math.log(2)) * ((4-1) / (2* (len(string5))) )
en_s3 = (1/math.log(2)) * ((4-1) / (2* (len(string3))) )


for seq in s5:
    for i,base in enumerate(seq):
        pos_list_s5[i][base] += 1


for seq in s3:
    for i,base in enumerate(seq):
        pos_list_s3[i][base] += 1

# print(pos_list_s3)
# print(pos_list_s5)


ht_s5 = []
for dicts in pos_list_s5:
    total = sum(dicts.values())
    Hi_s5 = 0
    for base,count in dicts.items():
        F_bi = count / total
        Hi_s5 -= (F_bi) * numpy.log2(F_bi)
    Ri_s5 = numpy.log2(4) - (Hi_s5 + en_s5)
    ht_s5.append({})
    for base,count in dicts.items():
        F_bi = count / total
        height = F_bi * Ri_s5
        ht_s5[-1][base] = height


ht_s3 = []
for dicts in pos_list_s3:
    total = sum(dicts.values())
    Hi_s3 = 0
    for base,count in dicts.items():
        F_bi = count / total
        Hi_s3 -= (F_bi) * numpy.log2(F_bi)
    Ri_s3 = numpy.log2(4) - (Hi_s3 + en_s3)
    ht_s3.append({})
    for base,count in dicts.items():
        F_bi = count / total
        height = F_bi * Ri_s3
        ht_s3[-1][base] = height

sort_ht_s5 = []
for dictionary in ht_s5:
    sorted5dict = sorted(dictionary.items() , key=lambda x:x[1] )
    sort_ht_s5.append(dict(sorted5dict))

sort_ht_s3 = []
for dictionary in ht_s3:
    sorted3dict = sorted(dictionary.items() , key=lambda x:x[1] )
    sort_ht_s3.append(dict(sorted3dict))


plt.style.use('BME163')

figureWidth = 5
figureHeight = 2
plt.figure(figsize=(figureWidth,figureHeight))

panel1height = 0.5
panel1width = 1.47
panel1 = plt.axes( [0.5/figureWidth , 0.6/figureHeight , panel1width/figureWidth , panel1height/figureHeight] )
xticks = [0 , 5 , 10 , 15 , 20]
xticklabels = ['-10', '-5', '0', '5' , '10']
panel1.set_xticks(xticks)
panel1.set_xticklabels(xticklabels)
panel1.set_xlabel('Distance to\nSplice Site')
panel1.set_ylabel('Bits')
panel1.set_title("5'SS")
panel1.set_xlim(0,20)
panel1.set_ylim(0,2)
panel1.axvline(x=10 , color= 'black' , linewidth = 0.5)
panel1.tick_params(bottom=True, labelbottom=True, left=True, labelleft=True, right=False, labelright=False,top=False, labeltop=False)


panel2height = 0.5
panel2width = 1.47
panel2 = plt.axes( [2.2/figureWidth , 0.6/figureHeight , panel2width/figureWidth , panel2height/figureHeight] )
xticks = [0 , 5 , 10 , 15 , 20]
xticklabels = ['-10', '-5', '0', '5' , '10']
panel2.set_xticks(xticks)
panel2.set_xticklabels(xticklabels)
panel2.set_xlabel('Distance to\nSplice Site')
panel2.set_title("3'SS")
panel2.set_xlim(0,20)
panel2.set_ylim(0,2)
panel2.axvline(x=10 , color= 'black' , linewidth = 0.5)
panel2.tick_params(bottom=True, labelbottom=True, left=False, labelleft=False, right=False, labelright=False,top=False, labeltop=False)


for xcoord,dictionary in enumerate(sort_ht_s5):
    ycoord = 0
    xcoord -= 0
    for nuc,height in dictionary.items():
        if nuc =='A':
            panel1.imshow(A, extent=[xcoord, xcoord + 1, ycoord, height + ycoord], aspect='auto', origin='upper')
        elif nuc =='T':
            panel1.imshow(T, extent=[xcoord, xcoord + 1, ycoord, height + ycoord], aspect='auto', origin='upper')
        elif nuc =='C':
            panel1.imshow(C, extent=[xcoord, xcoord + 1, ycoord, height + ycoord], aspect='auto', origin='upper')
        elif nuc=='G':
            panel1.imshow(G, extent=[xcoord, xcoord + 1, ycoord, height + ycoord], aspect='auto', origin='upper')
        ycoord += height
    xcoord += 1


for xcoord,dictionary in enumerate(sort_ht_s3):
    ycoord = 0
    xcoord -= 0
    for nuc,height in dictionary.items():
        if nuc =='A':
            panel2.imshow(A, extent=[xcoord, xcoord + 1 , ycoord , height + ycoord], aspect='auto', origin='upper')
        elif nuc =='T':
            panel2.imshow(T, extent=[xcoord, xcoord + 1, ycoord , height + ycoord], aspect='auto', origin='upper')
        elif nuc =='C':
            panel2.imshow(C, extent=[xcoord, xcoord + 1, ycoord , height + ycoord], aspect='auto', origin='upper')
        elif nuc=='G':
            panel2.imshow(G, extent=[xcoord, xcoord + 1, ycoord , height + ycoord], aspect='auto', origin='upper')
        ycoord += height
    xcoord += 1

plt.savefig('Patil_Sahil_BME163_Assignment_Week5.png' , dpi = 600)