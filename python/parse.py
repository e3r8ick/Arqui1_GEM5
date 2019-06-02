# Instituto Tecnologico de Costa Rica
# Arquitectura de Computadores 1
#
# Parser for GEM5's stats.txt file
#
# Josafat Vargas
# 21 of March, 2019

from fileManager import *


# Reads and parses a file with all the values we want to obtain from stats.txt
# BP types: LocalBP, TournamentBP, BiModeBP
# 
# Return: a vector with the identifiers of the variables
def getValuesVector (fileName):
    valuesVector = readFile(fileName)        
    valuesVector = valuesVector.split("\n")
    while("" in valuesVector) : 
        valuesVector.remove("")
    return valuesVector


# Turns a file into a matrix with m lines, each with r values
# r == 0: variable name
# r == 1: value of variable
# r >= 2: description of variable
#
# Return: an mxr matrix with all the values in the stats.txt file
def parse (fileName):
    matrix = []
    dta = readFile(fileName)
    
    # split into lines
    rows = dta.split("\n")
    rlen = len(rows)-3 # Adjust for file footer

    #split lines into values
    for i in range (2, rlen):# Adjust for file header
        matrix.append(rows[i].split (" "))

    #remove empty spaces
    mlen = len(matrix)
    for j in range(0, mlen):
        while("" in matrix[j]) : 
            matrix[j].remove("")
            
    return matrix


# Extracts the desired values (in valuesVector) from the parsed matrix
#
# Return: A matrix with 1st col: variable and 2nd col: value
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



# Prints the "data" column from the expected matrix
# data == 0: variable name
# data == 1: value of variable
# data >= 2: description of variable
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




# Takes the addres of a stats.txt files, and converts it into a matrix
# fileName: address of the file, relative to the app
#
# Return: the matrix with [variable, value] pairs
def runParser(fileName):
    valuesFile = "Files/searchValues.txt"
    valuesVector = getValuesVector(valuesFile)
    parsedFile = parse(fileName)
    clean = extract(parsedFile, valuesVector)
    #printMatrix(clean, 1)
    return clean

# Loads usable variable names for graphics
#
# Return: a vector with tags for the variables in the same order
def getTags():
    tagsFile = "Files/nameTags.txt"
    tagsVector = getValuesVector (tagsFile)
    return tagsVector


# Development test
def test():
    myFile = "Files/testStats.txt"
    runParser(myFile)
    return 0

