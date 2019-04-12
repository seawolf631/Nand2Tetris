import sys
import random
import os
import nltk

#Tokenizer
def tokenType(token):
    keywordList = ['class', 'constructor', 'function', 'method', 'field', 'static' , 'var', 'int', 'char','boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
    symbolList = ['{','}', '(',')', '[',']','.', ',',';','+','-','*','/','&','|','<','>','=','-']
    if(token in keywordList):
        return "keyword"
    elif(token in symbolList):
        return "symbol"
    elif(isinstance(token,int) and (int(token) >= 0) and (int(token) <= 32767) ):
        return "integerConstant"
    elif(token[0] == "\"" and token[-1] == "\"" ):
        return "STRING_CONST"
    else:
        return "identifier"

#def keyWord():

#def symbol():

#def identifier():

#def intVal():

#def stringVal():



#Start of Reading and Writing File

for n in sys.argv[1:]:
    fileName = n
    readFile = open(fileName, 'r')
    periodIndex = fileName.index(".")
    writeFile = open(fileName[:periodIndex] + "Ttest.xml" ,"a")
    fileContent = open(fileName).read()
    tokens = nltk.word_tokenize(fileContent)
    stringConst = False

    writeFile.write("<tokens>")
    for line in readFile:
        if line.strip() and (line[0:2] != "//") and (line[0:3] != "/**"):
            tokens = nltk.word_tokenize(line)
            for word in tokens:
                if word == "``":
                    stringConst = not stringConst
                    if stringConst:
                        writeFile.write("<stringConstant>")
                    if not stringConst:
                        writeFile.write("</stringConstant>")
                print stringConst
                if stringConst:
                    print word 
                    writeFile.write( word )
                elif word != "<" and word != ">" and word != "&":
                    print "\t<" + tokenType(word) + ">" + word + "</" + tokenType(word) + ">"
                    writeFile.write("\t<" + tokenType(word) + ">" + word + "</" + tokenType(word) + ">\n")
                elif word == ">":
                    writeFile.write("\t<" + tokenType(word) + ">" + "&gt;" + "</" + tokenType(word) + ">\n")
                elif word == "<":
                    writeFile.write("\t<" + tokenType(word) + ">" + "&lt;" + "</" + tokenType(word) + ">\n")
                elif word == "&":
                    writeFile.write("\t<" + tokenType(word) + ">" + "&amp;" + "</" + tokenType(word) + ">\n")
            #print tokens
            #print line

    writeFile.write("</tokens>")
    readFile.close()
    #writeFile.close()
