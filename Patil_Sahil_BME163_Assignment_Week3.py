import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy
import argparse
import matplotlib.patheffects as path_effects

parser = argparse.ArgumentParser()
parser.add_argument('--outputFile','-o',default='Assignment3.png',type=str,action='store',help='output file goes here')
parser.add_argument('--inputFile','-c',default='BME163_Input_Data_Week3.celltype.tsv',type=str,action='store',help='input file goes here')
parser.add_argument('--position','-p',default='BME163_Input_Data_Week3.position.tsv',type=str,action='store',help='input file goes here')

args = parser.parse_args()
outFile=args.outputFile
inFile=args.inputFile
print(outFile,inFile)

file2 = args.position

in_fh=open(inFile,'r')
in_fh2 = open(file2 , 'r')

xval = []
yval = []
barcodes = []
coordinates = {}

for i in in_fh2:
    barcode = i.rstrip().split()[0]
    xvalue = i.rstrip().split()[1]
    yvalue = i.rstrip().split()[2]

    xval.append(float(xvalue))
    yval.append(float(yvalue))
    barcodes.append(barcode)

    coordinates[barcode] = (float(xvalue) , float(yvalue))

# print(coordinates)

CellTYPES = {}
for line in in_fh:
    B_code = line.rstrip().split()[2]
    Cell = line.rstrip().split()[1]

    CellTYPES[B_code] = (Cell)

in_fh.close()
in_fh2.close()

# print(CellTYPES)

groupX = {CType:[] for CType in set(CellTYPES.values())}
groupY = {CType:[] for CType in set(CellTYPES.values())}
for barcode,position in coordinates.items():
    celltype = CellTYPES[barcode]
    x,y = position
    groupX[celltype].append(x)
    groupY[celltype].append(y)



plt.style.use('BME163')

figureWidth = 8
figureHeight = 4
plt.figure(figsize=(figureWidth,figureHeight))

panel1width = 1.35
panel1height = 1.35
panel1 = plt.axes( [0.5/figureWidth , 0.5/figureHeight , panel1width/figureWidth , panel1height/figureHeight] )

panel1.set_xlim(-30,30)
panel1.set_ylim(-40,30)

panel1.set_xlabel('tSNE 2')
panel1.set_ylabel('tSNE 1')


RB1=(225/255,13/255,50/255)
RB6=(143/255,138/255,86/255)
RB5=(248/255,177/255,61/255)
panel1.plot( groupX['monocyte'] , groupY['monocyte'] , marker = 'o' , markerfacecolor = RB6 , markeredgewidth = 0.25 , markersize = 4 , color = 'black' , linewidth = 0 )
panel1.plot( groupX['bCell'] , groupY['bCell'] , marker = 'o' , markerfacecolor = RB5 , markeredgewidth = 0.25 , markersize = 4 , color = 'black' , linewidth = 0 )
panel1.plot( groupX['tCell'] , groupY['tCell'] , marker = 'o' , markerfacecolor = RB1 , markeredgewidth = 0.25 , markersize = 4 , color = 'black' , linewidth = 0 )

panel1.text( numpy.median(groupX['monocyte']) , numpy.median(groupY['monocyte']) , 'monocyte' , fontsize = 8 , color = 'black' , style = 'normal' , va = 'center' , ha = 'center' , path_effects = [path_effects.Stroke(linewidth = 1.5 , foreground = 'white') , path_effects.Normal()])
panel1.text( numpy.median(groupX['bCell']) , numpy.median(groupY['bCell']) , 'bCell' , fontsize = 8 , color = 'black' , style = 'normal' , va = 'center' , ha = 'center' ,  path_effects = [path_effects.Stroke(linewidth = 1.5 , foreground = 'white') , path_effects.Normal()] )
panel1.text( numpy.median(groupX['tCell']) , numpy.median(groupY['tCell']) , 'tCell' , fontsize = 8 , color = 'black' , style = 'normal' , va = 'center' , ha = 'center' ,  path_effects = [path_effects.Stroke(linewidth = 1.5 , foreground = 'white') , path_effects.Normal()] )

plt.savefig('Patil_Sahil_BME163_Assignment_Week3.png' , dpi = 600)