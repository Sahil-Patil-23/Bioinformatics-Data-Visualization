import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--outputFile','-o',default='Assignment1.png',type=str,action='store',help='output file goes here')
parser.add_argument('--inputFile','-i',default='/path/toyour/data',type=str,action='store',help='input file goes here')

args = parser.parse_args()
outFile=args.outputFile
inFile=args.inputFile
print(outFile,inFile)

#Setting up the dimensions for the size of the entire figure
figureWidth = 5
figureHeight = 2
plt.figure(figsize=(figureWidth,figureHeight))

plt.style.use('BME163')

#Setting up the dimensions of the box with the circles in it
panelWidth = 1
panelHeight = 1
panel1 = plt.axes( [0.2/figureWidth , 0.2/figureHeight , panelWidth/figureWidth , panelHeight/figureHeight] )

#Setting up the x & y limits for the box with cirlces
panel1.set_ylim(0,16)
panel1.set_xlim(-1,14)

#These colors below are the ones that'll be used for the cirlces
RB1=(225/255,13/255,50/255)
RB2=(242/255,50/255,54/255)
RB3=(239/255,99/255,59/255)
RB4=(244/255,138/255,30/255)
RB5=(248/255,177/255,61/255)
RB6=(143/255,138/255,86/255)
RB7=(32/255,100/255,113/255)
RB8=(42/255,88/255,132/255)
RB9=(56/255,66/255,156/255)
RB10=(84/255,60/255,135/255)
RB11=(110/255,57/255,115/255)
RB12=(155/255,42/255,90/255)

colors = [(RB1),(RB2),(RB3),(RB4),(RB5),(RB6),(RB7),(RB8),(RB9),(RB10),(RB11),(RB12)]

#Creating the cirlces
for q in range(1,13):
    xvalues = []
    yvalues = []
    for r in np.arange(0 , 6.3 , 0.001):
        x = np.cos(r) + q
        y = np.sin(r) + 8
        xvalues.append(x)
        yvalues.append(y)

    #Plotting the cirlces with the appropriate colors & dimensions
    panel1.plot(xvalues,yvalues,
                marker = 'o',
                color = (colors[q-1]),
                markeredgewidth = 0,
                markersize = 0 ,
                linewidth = 1.15
                )
#Removes the labels around the box
panel1.tick_params(bottom=False, labelbottom=False,\
left=False, labelleft=False, \
right=False, labelright=False,\
top=False, labeltop=False)

#Setting up the dimensions of the boxes with the heatmaps
boxWidth = 2
boxHeight = 1
box1 = plt.axes([0.68/ boxWidth , 0.1/ boxHeight , boxWidth / figureWidth , boxHeight / figureHeight])

#Plotting the line in the box that separates the 2 compartments
box1.plot([-50, 150] , [1, 1 ] ,
          marker = '' ,
          color = 'black' ,
          lw = 0.75
          )
box1.set_ylim(0, 2)
box1.set_xlim(0, 100)

#These are the colors that are used for the bottom half of the box
viridis5 = (253/255, 231/255, 37/255)
viridis4 = (94/255, 201/255, 98/255)
viridis3 = (33/255, 145/255, 140/255)
viridis2 = (59/255, 82/255, 139/255)
viridis1 = (68/255, 1/255, 84/255)

#Setting up the R-values for the bottom half
r1 = np.linspace(viridis1[0], viridis2[0], 25)
r2 = np.linspace(viridis2[0], viridis3[0], 25)
r3 = np.linspace(viridis3[0], viridis4[0], 25)
r4 = np.linspace(viridis4[0], viridis5[0], 25)

#Setting up the B-values for the bottom half
b1 = np.linspace(viridis1[1], viridis2[1], 25)
b2 = np.linspace(viridis2[1], viridis3[1], 25)
b3 = np.linspace(viridis3[1], viridis4[1], 25)
b4 = np.linspace(viridis4[1], viridis5[1], 25)

#Setting up the G-values for the bottom half
g1 = np.linspace(viridis1[2], viridis2[2], 25)
g2 = np.linspace(viridis2[2], viridis3[2], 25)
g3 = np.linspace(viridis3[2], viridis4[2], 25)
g4 = np.linspace(viridis4[2], viridis5[2], 25)

#Concatenating the lists so the colors will blend properly
fullrlist = np.concatenate((r1, r2, r3, r4), axis=None)
fullblist = np.concatenate((b1, b2, b3, b4), axis=None)
fullglist = np.concatenate((g1, g2, g3, g4), axis = None)

#PLotting the bottom half with the appropriate colors & coordinate values
for ypos in range(0, 100, 1):
    rectangle = mplpatches.Rectangle([ypos,0], 1, 1,
                                     facecolor= (fullrlist[ypos] , fullblist[ypos] , fullglist[ypos]),
                                     edgecolor='black',
                                     linewidth= 0
                                     )
    box1.add_patch(rectangle)

#These are the colors that will be used for the top half of the heat map
plasma5 = (237/255, 252/255, 27/255)
plasma4 = (245/255, 135/255, 48/255)
plasma3 = (190/255, 48/255, 101/255)
plasma2 = (87/255, 0/255, 151/255)
plasma1 = (15/255, 0/255, 118/255)

#Setting up the R-values for the top half
R1 = np.linspace(plasma1[0],plasma2[0], 25)
R2 = np.linspace(plasma2[0],plasma3[0], 25)
R3 = np.linspace(plasma3[0],plasma4[0], 25)
R4 = np.linspace(plasma4[0],plasma5[0], 25)

#Setting up the G-values for the top half
G1 = np.linspace(plasma1[2],plasma2[2], 25)
G2 = np.linspace(plasma2[2],plasma3[2], 25)
G3 = np.linspace(plasma3[2],plasma4[2], 25)
G4 = np.linspace(plasma4[2],plasma5[2], 25)

#Setting up the B-values for the top half
B1 = np.linspace(plasma1[1],plasma2[1], 25)
B2 = np.linspace(plasma2[1],plasma3[1], 25)
B3 = np.linspace(plasma3[1],plasma4[1], 25)
B4 = np.linspace(plasma4[1],plasma5[1], 25)

#Concatenating the lists so the colors will blend properly
fullRlist = np.concatenate((R1, R2, R3, R4), axis= None )
fullGlist = np.concatenate((G1, G2, G3, G4), axis=None)
fullBlist = np.concatenate((B1, B2, B3, B4), axis=None)

#Plotting the top half of the box with the appropriate colors & coordinates
for ypos in range(0,100,1):
    rectangle = mplpatches.Rectangle([ypos, 1], 1, 1,
                                     facecolor=(fullRlist[ypos], fullBlist[ypos], fullGlist[ypos]),
                                     edgecolor='black',
                                     linewidth=0
                                     )
    box1.add_patch(rectangle)

#Removing labels from the heatmap
box1.tick_params(bottom=False, labelbottom=False,\
left=False, labelleft=False, \
right=False, labelright=False,\
top=False, labeltop=False)

#Saves all the changes made to the png file
plt.savefig('Patil_Sahil_BME163_Assignment_Week1.png' , dpi = 600)