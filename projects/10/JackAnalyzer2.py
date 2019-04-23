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
    if string in keywordList:
        return "keyword"

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
                splitCleanedLine = re.split("\s" , cleanedLine)
                if splitCleanedLine != ['']:
                    print(splitCleanedLine)

            tokenWriteFile.write("</tokens>")

            readFile.close()
            tokenWriteFile.close()
