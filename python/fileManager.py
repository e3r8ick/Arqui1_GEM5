# Instituto Tecnologico de Costa Rica
#
# Python file manager
#
# from fileManager import *
#
# Josafat Vargas
# 30 of May, 2019


# Manages the access and operaions in the external file
# fileName: file to be accessed
# mode: "r" to read, "w" to write (erases previous data), "a" appends data to file
# toWrite: anything if read, data to append/wrie
# return: 0 if failed
# return: 1 if succeded, overwrites/appends to fileName file
# return: data read if mode == "r"
def fileManager (fileName, mode, toWrite):
    #read and print file
    if (mode == "r"):
        file_object = open(fileName, mode)
        return file_object.read()
    #appends to file
    if (mode == "a"):
        file_object = open(fileName, mode)
        file_object.write(toWrite)
        return 0
        file_object.close()
    #Create a new file
    if (mode == "w"):
        file_object = open(fileName, mode)
        file_object.write(toWrite)
        return 0
        file_object.close()
    else:
        return 1



# Opens a txt file and captures it's contents
#
# str fileName: file to be accessed ie: "myfile.txt", "myFolder/myFile.txt"
# 
# return: string with data
def readFile (fileName):
    file_object = open(fileName, "r")
    read_data =  file_object.read()
    file_object.close()
    return read_data



# Creates a new text file and fills it with data. It overwrites exisiting files
#
# str fileName: file to be accessed ie: "myfile.txt", "myFolder/myFile.txt".
#               creates a file if it doesn't exist
# str toWrite: data to write the file
# 
# return: 0 when done
def writeFile (fileName, toWrite):
    file_object = open(fileName, "w")
    file_object.write(toWrite)
    file_object.close()
    return 0


# Appends data to an already existing file
#
# str fileName: file to be accessed ie: "myfile.txt", "myFolder/myFile.txt".
# str toWrite: data to write the file
# 
# return: 0 when done
def appendFile (fileName, toWrite):
    file_object = open(fileName, "a")
    file_object.write(toWrite)
    file_object.close()
    return 0



# Test
# Create a file, and write to it. Append to file. Read file
#
# Return 0 if test succeds, else 1

def test ():
    writeFile("test.txt", "Hello ")
    appendFile("test.txt", "World!")
    readTest = readFile("test.txt")
    if (readTest == "Hello World!"):
        return 0
    else:
        return 1




























    
       
