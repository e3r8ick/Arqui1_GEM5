# Instituto Tecnologico de Costa Rica
# Arquitectura de Computadores 1
#
# Parser for GEM5's stats.txt file
#
# Josafat Vargas
# 21 of March, 2019

from fileManager import *


# Turns a file into a matrix with m lines, each with r values
# r == 0: variable name
# r == 1: value of variable
# r >= 2: description of variable
def parse (fileName):
    dta = readFile(myFile)
    matrix = []

    # split into lines
    rows = dta.split("\n")
    rlen = len(rows)

    #split lines into values
    for i in range (0, rlen):
        matrix.append(rows[i].split (" "))
        #remove empty spaces
        while("" in matrix[i]) : 
            matrix[i].remove("")

    return matrix


# r == 0: variable name
# r == 1: value of variable
# r >= 2: description of variable
def printMatrix(matrix, data):
    mlen = len(matrix)
    if (data < 2):
        for i in range (0, mlen):
            print (matrix[i][data])
    else:
        for i in range (0, mlen):
            rlen = len(matrix[i])
            info = ""
            for j in range (2, rlen):
                info += matrix[i][j] + " "
            print (info)



def extract(matrix, valuesVector):
    vlen = len(valuesVector)
    mlen = len(matrix)-1
    out = []
    for x in range(0, vlen):
        for i in range (0, mlen):
            if (valuesVector[x] == matrix[i][0]):
                out.append([ matrix[i][0], matrix[i][1] ])
                break
    return out

#Test values
a = "sim_insts"
b = "sim_ops"
c = "system.clk_domain.voltage_domain.voltage"
vV = [a, b, c]

myFile = "Files/test.txt"
matrix = parse(myFile)
clean = extract(matrix, vV)
print(clean)








mlen = len(matrix)  # all lines
rlen = 0            # every row will have different length
