import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--outputFile','-o',default='Assignment4.png',type=str,action='store',help='output file goes here')
parser.add_argument('--coverage','-c',default='BME163_Input_Data_4.cov',type=str,action='store',help='input file goes here')
parser.add_argument('--identity','-i',default='BME163_Input_Data_4.ident',type=str,action='store',help='input file goes here')

args = parser.parse_args()
outFile=args.outputFile
inFile=args.coverage
print(outFile,inFile)

file2 = args.identity

in_fh=open(inFile,'r')
in_fh2 = open(file2 , 'r')

Barcodes = []
Coverages = []
barcode_and_coverage = {}

count = 0
count4_6 = 0
count7_9 = 0
count10above = 0
for i , line in enumerate(in_fh):
    barcode = line.rstrip().split('\t')[0]
    coverage = line.rstrip().split('\t')[1]

    if int(coverage) >= 1 and int(coverage) <= 3:
        if count >= 1000:
            continue

        Barcodes.append(barcode)
        Coverages.append(coverage)
        barcode_and_coverage[barcode] = (coverage)
        count += 1

    if int(coverage) >= 4 and int(coverage) <= 6:
        if count4_6 >= 1000:
            continue

        Barcodes.append(barcode)
        Coverages.append(coverage)
        barcode_and_coverage[barcode] = (coverage)
        count4_6 += 1

    if int(coverage) >= 7 and int(coverage) <= 9:
        if count7_9 >= 1000:
            continue

        Barcodes.append(barcode)
        Coverages.append(coverage)
        barcode_and_coverage[barcode] = (coverage)
        count7_9 += 1

    if int(coverage) >= 10:
        if count10above >= 1000:
            continue

        Barcodes.append(barcode)
        Coverages.append(coverage)
        barcode_and_coverage[barcode] = (coverage)
        count10above += 1

# print(barcode_and_coverage)
# print(len(barcode_and_coverage))

barcode_and_identity = {}
for i , line in enumerate(in_fh2):
    Barcode = line.rstrip().split('\t')[0]
    Identity = line.rstrip().split('\t')[1]

    if Barcode in barcode_and_coverage.keys():
        barcode_and_identity[Barcode] = (float(Identity))


coverages = ['1-3' , '4-6' , '7-9' , '>=10']
Xval = {group:[] for group in coverages}
for barcode,coverage in barcode_and_coverage.items():
    ID = barcode_and_identity[barcode]

    if int(coverage) <= 3:
        Xval['1-3'].append(ID)

    if int(coverage) >= 4 and int(coverage) <=6:
        Xval['4-6'].append(ID)

    if int(coverage) >= 7 and int(coverage) <=9:
        Xval['7-9'].append(ID)

    if int(coverage) >= 10:
        Xval['>=10'].append(ID)

# print(Xval['1-3'])

plt.style.use('BME163')

figureWidth = 5
figureHeight = 5
plt.figure(figsize=(figureWidth,figureHeight))

panel1height = 4
panel1width = 3
panel1 = plt.axes( [0.5/figureWidth , 0.75/figureHeight , panel1width/figureWidth , panel1height/figureHeight] )

panel1.set_xlabel('Identity (%)')
panel1.set_ylabel('Subread Coverage')

yticks = [1.125 , 3.375 , 5.625 , 7.875]
yticklabels = ['1-3', '4-6', '7-9', '>=10']
panel1.set_yticks(yticks)
panel1.set_yticklabels(yticklabels)

iBlue=(44/255,86/255,134/255)
iOrange=(230/255,87/255,43/255)
iYellow=(248/255,174/255,51/255)
iGreen=(32/255,100/255,113/255)

def swarmplot(YPos, Xval, panel1, color):
    placedpoints = []
    xmin = 75
    xmax = 100
    ymin = 0
    ymax = 9
    width = 0.4
    panelwidth = 3
    panelheight = 4
    xrange = xmax - xmin
    yrange = ymax - ymin
    markerSize = 1
    mindist = markerSize/72
    shift = ((mindist/5) * xrange) / panelwidth

    for x1 in Xval:
        placed = False
        if len(placedpoints) == 0:
            placedpoints.append((YPos,x1))
        else:
            for move in numpy.arange(0,width,shift):
                y1 = YPos + (move*numpy.random.choice((-1,1)))
                distlist = []

                for coords2 in placedpoints:
                    x2, y2 = coords2[0], coords2[1]
                    xdist = (numpy.abs(x1 - x2) / xrange) * panelwidth
                    ydist = (numpy.abs(y1 - y2) / yrange) * panelheight
                    distance = (xdist ** 2 + ydist ** 2) ** 0.5
                    distlist.append(distance)

                if min(distlist) > mindist:
                    #placedpoints.append( (xpos,ypos,qual) )
                    #placed = True
                    #break
                    placed = True
                    break

            if placed:
                placedpoints.append((x1,y1))
            else:
                break
            # print(placedpoints)

            for coords in placedpoints:
                x,y = coords[0] , coords[1]
                panel1.plot(x,y,marker = 'o',mew=0,mfc=color, ms = markerSize)
        # swarmplot(1, Xval['1-3'][:100], panel1, iBlue)

panel1.set_xlim(75,100)
panel1.set_ylim(0,9)

swarmplot(1.1,Xval['1-3'][:1000],panel1, iBlue)

swarmplot(3.4,Xval['4-6'][:1000],panel1, iGreen)

swarmplot(5.63,Xval['7-9'][:1000],panel1, iYellow)

swarmplot(7.8,Xval['>=10'][:1000],panel1, iOrange)

plt.savefig('Patil_Sahil_BME163_Assignment_Week4.png' , dpi = 600)
