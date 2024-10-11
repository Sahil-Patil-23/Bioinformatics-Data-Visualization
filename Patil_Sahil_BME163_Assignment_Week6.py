import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import matplotlib.image as mpimg
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--outputFile','-o',default='Assignment4.png',type=str,action='store',help='output file goes here')
parser.add_argument('--exp','-e',default='BME163_Input_Data_Assignment6.exp',type=str,action='store',help='input file goes here')
parser.add_argument('--phase','-p',default='BME163_Input_Data_Assignment6.phase',type=str,action='store',help='input file goes here')

args = parser.parse_args()
outFile=args.outputFile
File1=args.exp
File2 =args.phase

plt.style.use('BME163')

figureWidth = 5
figureHeight = 3
plt.figure(figsize=(figureWidth,figureHeight))

panel1height = 2.5
panel1width = 0.75
panel1 = plt.axes( [0.5/figureWidth , 0.3/figureHeight , panel1width/figureWidth , panel1height/figureHeight] )
panel1.set_xlabel('CT')
panel1.set_ylabel('Number of genes')
panel1.set_ylim(0,1263)
panel1.set_xlim(0,23)
xticks = [0,3,6,9,12,15,18,21]
xticklabels = ['0' , '' , '6' , '' , '12' , '' , '18' , '']
panel1.set_xticks(xticks)
panel1.set_xticklabels(xticklabels)
panel1.tick_params(bottom=True, labelbottom=True, left=True, labelleft=True, right=False, labelright=False,top=False, labeltop=False)

legendheight = 0.2
legendwidth = 0.1
legend = plt.axes( [1.3/figureWidth , 1.45/figureHeight , legendwidth/figureWidth , legendheight/figureHeight] )
legend.set_ylim(0,100)
yticks = [0 , 100]
yticklabels = ['Min' , 'Max']
legend.set_yticks(yticks)
legend.set_yticklabels(yticklabels)
legend.tick_params(bottom=False, labelbottom=False, left=False, labelleft=False, right=True, labelright=True,top=False, labeltop=False)

viridis5 = (253/255, 231/255, 37/255)
viridis4 = (94/255, 201/255, 98/255)
viridis3 = (33/255, 145/255, 140/255)
viridis2 = (59/255, 82/255, 139/255)
viridis1 = (68/255, 1/255, 84/255)
R1=np.linspace(viridis1[0],viridis2[0],26)
G1=np.linspace(viridis1[1],viridis2[1],26)
B1=np.linspace(viridis1[2],viridis2[2],26)

R2=np.linspace(viridis2[0],viridis3[0],26)
G2=np.linspace(viridis2[1],viridis3[1],26)
B2=np.linspace(viridis2[2],viridis3[2],26)

R3=np.linspace(viridis3[0],viridis4[0],26)
G3=np.linspace(viridis3[1],viridis4[1],26)
B3=np.linspace(viridis3[2],viridis4[2],26)

R4=np.linspace(viridis4[0],viridis5[0],26)
G4=np.linspace(viridis4[1],viridis5[1],26)
B4=np.linspace(viridis4[2],viridis5[2],26)

R=np.concatenate((R1[:-1],R2[:-1],R3[:-1],R4),axis=None)
G=np.concatenate((G1[:-1],G2[:-1],G3[:-1],G4),axis=None)
B=np.concatenate((B1[:-1],B2[:-1],B3[:-1],B4),axis=None)

for y in range(0, 100, 1):
    rectangle = mplpatches.Rectangle([0, y], 1, 1,
                                     facecolor= (R[y] , G[y] , B[y]), edgecolor='black', linewidth= 0)
    legend.add_patch(rectangle)

ID_FPKM_dict = {}
with open(File1 , 'r') as file1:
    next(file1)
    for line in file1:
        ID = line.rstrip().split('\t')[1]
        FPKM_CT0 = line.rstrip().split('\t')[4]
        FPKM_CT3 = line.rstrip().split('\t')[5]
        FPKM_CT6 = line.rstrip().split('\t')[6]
        FPKM_CT9 = line.rstrip().split('\t')[7]
        FPKM_CT12 = line.rstrip().split('\t')[8]
        FPKM_CT15 = line.rstrip().split('\t')[9]
        FPKM_CT18 = line.rstrip().split('\t')[10]
        FPKM_CT21 = line.rstrip().split('\t')[11]

        ID_FPKM_dict[ID] = ( float(FPKM_CT0) , float(FPKM_CT3) , float(FPKM_CT6) , float(FPKM_CT9) ,
                             float(FPKM_CT12) , float(FPKM_CT15) , float(FPKM_CT18) , float(FPKM_CT21) )

ID_phase_dict = {}
with open(File2 , 'r') as file2:
    next(file2)
    for line in file2:
        ID = line.rstrip().split('\t')[0]
        phase = line.rstrip().split('\t')[1]

        ID_phase_dict[ID] = (float(phase))
    ID_phase_dict2 = sorted(ID_phase_dict.items() , key = lambda x:x[1])
    len_of_genes = len(ID_phase_dict2)

for i,v in enumerate(ID_phase_dict2):
    val_list = list(v)
    ypos = i
    val_list.append(ypos)
    ID_phase_dict2[i] = val_list

y= len_of_genes
for id,phase,i in ID_phase_dict2:
    FPKM = ID_FPKM_dict[id]
    y -= 1
    x = 0
    for val in range(len(FPKM)):
        # print(FPKM[val])
        normalized_data = ( (FPKM[val] - min(FPKM)) / (max(FPKM) - min(FPKM)) ) * 100
        # print(normalized_data)
        color_data = int(normalized_data)
        rectangle = mplpatches.Rectangle([x , y], 3, 1,
                                         facecolor=( R[color_data] , G[color_data] , B[color_data] ),
                                         edgecolor= 'black',
                                         linewidth= 0)
        x += 3

        panel1.add_patch(rectangle)

plt.savefig('Patil_Sahil_BME163_Assignment_Week6.png' , dpi = 600)