import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--outputFile','-o',default='Assignment2.png',type=str,action='store',help='output file goes here')
parser.add_argument('--inputFile','-i',default='BME163_Input_Data_1.txt',type=str,action='store',help='input file goes here')
parser.add_argument('--outTextFile','-t',default='BME163_Input_Data_1.txt',type=str,action='store',help='output file goes here')

args = parser.parse_args()
outFile=args.outputFile
inFile=args.inputFile
print(outFile,inFile)

plt.style.use('BME163')

XValues = []
YValues = []

in_fh=open(inFile,'r')

for line in in_fh:
    l = line.rstrip().split('\t')
    XValues.append(numpy.log2(float(l[1])+1))
    YValues.append(numpy.log2(float(l[2])+1))

in_fh.close()

figureWidth = 5
figureHeight = 2
plt.figure(figsize=(figureWidth,figureHeight))

panelWidth = 1
panelHeight = 1
panel1 = plt.axes( [0.7/figureWidth , 0.3/figureHeight , panelWidth/figureWidth , panelHeight/figureHeight] )

panel1.set_xlim(0,15)
panel1.set_ylim(0,15)

iYellow=(248/255,174/255,51/255)

panel1.plot(XValues,YValues,
marker='o',
markerfacecolor= iYellow,
markeredgewidth=0,
markersize=1.57,
color='black',
linewidth=0,
alpha=0.042)

panel1.tick_params(bottom=True, labelbottom=True,left=False, labelleft=False, right=False, labelright=False,top=False, labeltop=False)

sidepanel1width = 0.25
sidepanel1height = 1
sidepanel1 = plt.axes( [0.019/sidepanel1width , 0.15/sidepanel1height , sidepanel1width/figureWidth , sidepanel1height/figureHeight] )

sidepanel1.set_ylim(0,15)
sidepanel1.set_xlim(20,0)

iBlue=(88/255,85/255,120/255)

sidebins = numpy.linspace(0,20,41)

sidehisto , sidebins = numpy.histogram(YValues , sidebins)

for i in range(0 , len(sidehisto) , 1):
    left = sidebins[i]
    bottom = 0
    width = numpy.log2((sidehisto[i]) + 1)
    height = (sidebins[i+1] - left)

    rectangle = mplpatches.Rectangle([bottom,left],width,height,
                                     facecolor= iBlue,
                                     edgecolor= 'black',
                                     linewidth=0.301
                                     )
    sidepanel1.add_patch(rectangle)

sidepanel1.tick_params(bottom=True, labelbottom=True, left=True, labelleft=True, right=False, labelright=False,top=False, labeltop=False)

toppanel1width = 1
toppanel1height = 0.25
toppanel1 = plt.axes([0.14/toppanel1width , 0.1713/toppanel1height , toppanel1width/figureWidth , toppanel1height/figureHeight])

iGreen=(120/255,172/255,145/255)

toppanel1.set_ylim(0,20)
toppanel1.set_xlim(0,15)

topbins = numpy.linspace(0,15,31)

tophisto , topbins = numpy.histogram(XValues , topbins)

for i in range(0, len(tophisto) , 1):
    left = topbins[i]
    bottom = 0
    width = topbins[i+1] - left
    height = numpy.log2((tophisto[i]) + 1)

    rectangle = mplpatches.Rectangle([left, bottom], width, height,
                                     facecolor=iGreen,
                                     edgecolor='black',
                                     linewidth=0.311
                                     )
    toppanel1.add_patch(rectangle)

toppanel1.tick_params(bottom=False, labelbottom=False,left=True, labelleft=True, right=False, labelright=False,top=False, labeltop=False)

plt.savefig('Patil_Sahil_BME163_Assignment_Week2' , dpi = 600)