import numpy as np
import matplotlib.pyplot as plt

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

barPlot("sample plot", [45,78,85,56,68],"values",['one','two','three','four','five'])