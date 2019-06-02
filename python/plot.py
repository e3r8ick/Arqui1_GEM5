
import numpy as np
import matplotlib.pyplot as plt
from parse import *

''' 
    groupBarPlot function takes: 
        arg title: title for the plot
        arg data:   matrix with data to be displayed on the bars. 
                    A column contains all data for one group(same benchmark). 
                    A row contains the same data of all groups 
                    (Same value of parameter being tested
                    e.g Icache=512Kb).
        arg ylabel: y axis label (name of variable being displayed
                    e.g MissRate)
        arg groupLabels: Group Label (name of benchmark e.g Queens)
        arg barLabels: labels for the bars (parameter value eg Icache=512Kb)
        arg colors: colors for the bars
'''


def groupBarPlot(title, data, ylabel, groupLlabels, barLabels, colors):
    #define the plot figure
    fig, ax = plt.subplots()
    
    #setup dimension variables
    ind = np.arange(len(data)) #position for the grops
    ind = ind * len(groupLlabels)
    width = 0.5  # the width of the bars
    
    #drawing individual bars
    for col in data:
        
        drawSubPlot(ax, ind, col, width, barLabels)
    
    #setting general plot labels
    ax.set_xticklabels(['']+[barLabels[0]])
    ax.set_title(title)
    plt.show()


def drawSubPlot(ax, ind, dataVector, width, label):
    ax.bar(ind, dataVector, align='center', width=width)






groupBarPlot("sample plot", [float(M64[1][1]), float(M128[1][1])], "values", [M64[1][0], M128[1][0]],getTags(),2)


