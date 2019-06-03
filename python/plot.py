
import numpy as np
import matplotlib.pyplot as plt
from parse import *

import matplotlib as plt2
plt2.rcParams.update({'figure.max_open_warning': 0})

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
'''


def groupBarPlot(title, data, ylabel, groupLlabels, barLabels):
    #define the plot figure
    fig, ax = plt.subplots()
    
    #setup dimension variables
    ind = np.arange(len(data[0])) #position for the grops
    width = 1  # the width of the bars
    
    #drawing individual bars
    count=0
    for row in data:
        drawSubPlot(ax,2*len(barLabels) * ind - (count+1) , row, width, barLabels[count])
        count += 1
    
    #setting plot's general labels
    ax.set_xticks(2*len(barLabels)*ind-len(barLabels))
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(groupLlabels)
    ax.set_title(title)
    ax.legend()
    
    plt.savefig("graficos/"+title+' '+ylabel+'.png')


def drawSubPlot(ax, ind, dataVector, width, label):
    
    ax.bar(ind, dataVector, align='center', width=width,label=label)



# groupBarPlot("sample plot", [[5,20,7],[7,14,10],[15,9,6]], "misses",['Queens','Perm','IntMM'],['512','256','128'])

# groupBarPlot("sample plot", [[5,20,7],[7,14,10],[15,9,6],[11,9,5]], "misses",['Queens','Perm','IntMM'],['512','256','128','64'])

# groupBarPlot("sample plot", [[5,20],[7,14],[12,7]], "misses",['Queens','Perm'],['512','256','128'])


#groupBarPlot("sample plot", [[5,20,7,11,9,13],[7,14,10,3,7,6],[15,9,6,10,8,2],[11,9,5,14,3,10]], "misses",['Queens','Perm','IntMM','FloatMM','Towers','Tree'],['512','256','128','64'])

#M64 = runParser("../gem5/se_results/Queens_cache_line_size64/stats.txt")
