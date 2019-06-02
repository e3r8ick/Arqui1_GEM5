
import numpy as np
import matplotlib.pyplot as plt
from parse import *

''' 
    groupBarPlot function takes: 
        arg title: title for the plot
        arg data:   matrix with data to be displayed on the bars. 
                    A row contains all data for one group(same benchmark). 
                    A column contains the same data of all groups 
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






M64 = runParser("../../se_results/Queens_cache_line_size64/stats.txt")
M128 = runParser("../../se_results/Queens_cache_line_size128/stats.txt")

# M[numero de variable][1=dato, 0 = nombre largo de variable q no se usa] 
print(M64[1][0])
print(float(M64[1][1]))
print('tags')
print(getTags())

a=['a','b','c']
b=[1,2,3]

for (z,x) in (a,b):
    print(z)
    print(x)

groupBarPlot("sample plot", [float(M64[1][1]), float(M128[1][1])], "values", [M64[1][0], M128[1][0]],getTags(),2)


