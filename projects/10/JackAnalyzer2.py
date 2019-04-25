import sys
import os
import re


#Function to Remove Comments from Line
def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
    return string

#Function to Determine Type of Token
def tokenType(string):
    keywordList = ['class','constructor','function','method','field','static','var','int','char','boolean','void','true','false','null','this','let','do','if','else','while','return']
    symbolList = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~']
    if string in keywordList:
        return "keyword"
    elif string in symbolList:
        return "symbol"
    elif string.isdigit():
        return "integerConstant"
    else:
        return "identifier"

#Reading & Writing File
for n in sys.argv[1:]:
    directory = n
    for fileName in os.listdir(directory):
        if fileName.endswith(".jack"):
            readFile = open(directory + "/" + fileName, "r")
            periodIndex = fileName.index(".")
            tokenWriteFile = open(directory + "/" + fileName[:periodIndex] + "Ttest.xml", "a")
            
            tokenWriteFile.write("<tokens>")

            #Going through Line by Line of ReadFile
            for line in readFile:
                noCommentsLine = removeComments(line)
                cleanedLine = noCommentsLine.strip()
                #Adding Space Before & After Symbols
                addSpaceBefore = re.sub(r"(\(|\)|\-|\.|\;|\[|\])",r" \1 ",cleanedLine)
                splitCleanedLine = addSpaceBefore.split()
                if splitCleanedLine != []:
                    print(splitCleanedLine)
                    for string in splitCleanedLine:
                        tokenWriteFile.write("<" + tokenType(string) + ">" + string + "</" + tokenType(string) + ">\n")

            tokenWriteFile.write("</tokens>")

            readFile.close()
            tokenWriteFile.close()
