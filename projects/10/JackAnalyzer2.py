import sys
import os
import re


#Function to Remove Comments from Line
def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
    string = re.sub(re.compile("/\*\*.*") , "", string)
    string = re.sub(re.compile("^\s\*.*") , "", string)
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

#Function to Transform Symbol Token into XML form
def symbolTransform(string):
    if tokenType(string) == "symbol":
        if string == "<":
            return "&lt;"
        elif string == "&":
            return "&amp;"
        elif string == ">":
            return "&gt;"
        else:
            return string
    else:
        return string

#Reading & Writing File
for n in sys.argv[1:]:
    directory = n
    for fileName in os.listdir(directory):
        if fileName.endswith(".jack"):
            readFile = open(directory + "/" + fileName, "r")
            periodIndex = fileName.index(".")
            tokenWriteFile = open(directory + "/" + fileName[:periodIndex] + "Ttest.xml", "a")
            
            tokenWriteFile.write("<tokens>\n")

            #Going through Line by Line of ReadFile
            for line in readFile:
                noCommentsLine = removeComments(line)
                cleanedLine = noCommentsLine.strip()
                #Adding Space Before & After Symbols
                #retrieveStrings = re.sub(r"\"", r"  ",cleanedLine)
                addSpaceBefore = re.sub(r"(\(|\)|\-|\.|\;|\[|\]|,|~)",r" \1 ",cleanedLine)
                splitCleanedLine = addSpaceBefore.split()
                if splitCleanedLine != []:
                    print(splitCleanedLine)
                    isString = False
                    for string in splitCleanedLine:
                        if(string[0] == "\"" or string[-1]=="\""):
                            isString = not isString
                            if isString:
                                tokenWriteFile.write("<stringConstant>" + string[1:] + " ")
                            elif not isString:
                                tokenWriteFile.write(string[:-1] + "</stringConstant>\n")
                        elif(isString and string[-1] != "\""):
                            tokenWriteFile.write(string + " ")
                        else:
                            tokenWriteFile.write("<" + tokenType(string) + ">" + symbolTransform(string) + "</" + tokenType(string) + ">\n")

            tokenWriteFile.write("</tokens>")

            readFile.close()
            tokenWriteFile.close()
