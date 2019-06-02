
import numpy as np
import matplotlib.pyplot as plt

from parse import *
''' 
    barPlot function takes: 
        arg title: title for the plot
        arg data: array with data to be displayed on the bars
        arg ylabel: y axis label
        arg xlabels: labels for each bar on x axis
'''
def barPlot(title, data, ylabel,xlabels):
    fig, ax = plt.subplots()
    x_pos = np.arange(len(data))
    ax.bar(x_pos, data, align='center')
    ax.set_xticklabels(['']+xlabels)   
    ax.set_title(title)
    plt.show()


M64 = runParser("../../se_results/Queens_cache_line_size64/stats.txt")
M128 = runParser("../../se_results/Queens_cache_line_size128/stats.txt")



print(M64[16][0])
print(float(M64[16][1]))



barPlot("sample plot", [float(M64[16][1]),float(M128[16][1])],"values",[M64[16][0],M128[16][0]])