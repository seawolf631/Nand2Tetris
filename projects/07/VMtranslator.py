import sys
import random
#Necessary Parser and CodeWriter Methods
def commandType(currentLine):
    lineList = currentLine.split()
    if len(lineList) == 1:
        return "C_ARITHMETIC"
    elif lineList[0] == "pop":
        return "C_POP"
    elif lineList[0] == "push":
        return "C_PUSH"
def arg1(currentLine):
    firstSpace = currentLine.index(" ")
    secondSpace = currentLine[(firstSpace+1):].index(" ") + firstSpace + 1
    return currentLine[firstSpace+1: secondSpace]
def arg2(currentLine):
    firstSpace = currentLine.index(" ")
    secondSpace = currentLine[(firstSpace+1):].index(" ") + firstSpace + 1
    return currentLine[secondSpace+1:]
def writeArithmetic(currentLine):
    lineList = currentLine.split()
    labelNum = str(100+(1000*random.randint(0,100)))
    labelNum2 = str(int(labelNum) + 1)
    if(lineList[0] == "add"):
        writeFile.write("//Adding\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("D=M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("A=M\n")
        writeFile.write("M=M+D\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "sub"):
        writeFile.write("//Subtracting\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("D=M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("A=M\n")
        writeFile.write("M=M-D\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "eq"):
        writeFile.write("//Equals\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("D=M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("A=M\n")
        writeFile.write("D=A-D\n")
        writeFile.write("@EQUAL" + str(labelNum)+ "\n")
        writeFile.write("D;JEQ\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("M=0\n")
        writeFile.write("@EQUAL" +str(labelNum2)+ "\n")
        writeFile.write("0;JMP\n")
        writeFile.write("(EQUAL" + str(labelNum)+")\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("M=-1\n")
        writeFile.write("(EQUAL"+str(labelNum2)+")\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "lt"):
        writeFile.write("//Less-Than\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("D=M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("A=M\n")
        writeFile.write("D=A-D\n")
        writeFile.write("@LESSTHAN" + str(labelNum)+ "\n")
        writeFile.write("D;JLT\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("M=0\n")
        writeFile.write("@LESSTHAN" +str(labelNum2)+ "\n")
        writeFile.write("0;JMP\n")
        writeFile.write("(LESSTHAN" + str(labelNum)+")\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("M=-1\n")
        writeFile.write("(LESSTHAN"+str(labelNum2)+")\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "gt"):
        writeFile.write("//Greather-Than\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("D=M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("A=M\n")
        writeFile.write("D=A-D\n")
        writeFile.write("@GREATERTHAN" + str(labelNum)+ "\n")
        writeFile.write("D;JGT\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("M=0\n")
        writeFile.write("@GREATERTHAN" +str(labelNum2)+ "\n")
        writeFile.write("0;JMP\n")
        writeFile.write("(GREATERTHAN" + str(labelNum)+")\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("M=-1\n")
        writeFile.write("(GREATERTHAN"+str(labelNum2)+")\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "neg"):
        writeFile.write("//Negate\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("A=M\n")
        writeFile.write("M=-M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "or"):
        writeFile.write("//OR\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("A=A-1\n")
        writeFile.write("A=A-1\n")
        writeFile.write("D=M\n")
        writeFile.write("A=A+1\n")
        writeFile.write("D=D|M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("M=M-1\n")
        writeFile.write("A=M\n")
        writeFile.write("M=D\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
    elif(lineList[0] == "not"):
        writeFile.write("//NOT\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("A=A-1\n")
        writeFile.write("D=M\n")
        writeFile.write("D=!D\n")
        writeFile.write("M=D\n")
    elif(lineList[0] == "and"):
        writeFile.write("//AND\n")
        writeFile.write("@SP\n")
        writeFile.write("A=M\n")
        writeFile.write("A=A-1\n")
        writeFile.write("A=A-1\n")
        writeFile.write("D=M\n")
        writeFile.write("A=A+1\n")
        writeFile.write("D=D&M\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M-1\n")
        writeFile.write("M=M-1\n")
        writeFile.write("A=M\n")
        writeFile.write("M=D\n")
        writeFile.write("@SP\n")
        writeFile.write("M=M+1\n")
def writePushPop(commandType, segment, index):
    if(commandType == "C_PUSH"):
        if(segment == "constant"):
            writeFile.write("//Pushing\n")
            writeFile.write("@"+index)
            writeFile.write("D=A\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "argument"):
            writeFile.write("//Pushing with Argument\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@ARG\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("A=D\n")
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "local"):
            writeFile.write("//Pushing with Local\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@LCL\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("A=D\n")
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "that"):
            writeFile.write("//Pushing with That\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@THAT\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("A=D\n")
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "temp"):
            index = str(int(index) + 3)
            writeFile.write("//Pushing with Temp\n")
            writeFile.write("@" + index+ "\n")
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "this"):
            writeFile.write("//Pushing with This\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@THIS\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("A=D\n")
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "pointer"):
            index = str(int(index) + 3)
            writeFile.write("//Pushing with Pointer\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
        elif(segment == "static"):
            writeFile.write("//Pushing with Static\n")
            writeFile.write("@" + fileName[-8:periodIndex] + "." + index)
            writeFile.write("D=M\n")
            writeFile.write("@SP\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M+1\n")
    elif(commandType == "C_POP"):
        if(segment == "constant"):
            writeFile.write("//Popping with Constant\n")
            writeFile.write("@SP")
        elif(segment == "that"):
            writeFile.write("//Popping with That\n")
            writeFile.write("@" + index +"\n")
            writeFile.write("D=A\n")
            writeFile.write("@THAT\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("@THAT\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@THAT\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@THAT\n")
            writeFile.write("A=M\n")
            writeFile.write("D=A-D\n")
            writeFile.write("@THAT\n")
            writeFile.write("M=D\n")
        elif(segment == "this"):
            writeFile.write("//Popping with This\n")
            writeFile.write("@" + index +"\n")
            writeFile.write("D=A\n")
            writeFile.write("@THIS\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("@THIS\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@THIS\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@THIS\n")
            writeFile.write("A=M\n")
            writeFile.write("D=A-D\n")
            writeFile.write("@THIS\n")
            writeFile.write("M=D\n")
        elif(segment == "argument"):
            writeFile.write("//Popping with Argument\n")
            writeFile.write("@" + index +"\n")
            writeFile.write("D=A\n")
            writeFile.write("@ARG\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("@ARG\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@ARG\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@ARG\n")
            writeFile.write("A=M\n")
            writeFile.write("D=A-D\n")
            writeFile.write("@ARG\n")
            writeFile.write("M=D\n")
        elif(segment == "local"):
            writeFile.write("//Popping with Local\n")
            writeFile.write("@" + index +"\n")
            writeFile.write("D=A\n")
            writeFile.write("@LCL\n")
            writeFile.write("A=M\n")
            writeFile.write("D=D+A\n")
            writeFile.write("@LCL\n")
            writeFile.write("M=D\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@LCL\n")
            writeFile.write("A=M\n")
            writeFile.write("M=D\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("D=A\n")
            writeFile.write("@LCL\n")
            writeFile.write("A=M\n")
            writeFile.write("D=A-D\n")
            writeFile.write("@LCL\n")
            writeFile.write("M=D\n")
        elif(segment == "temp"):
            index = str(int(index) + 5)
            writeFile.write("//Popping with Temp\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("M=D\n")
        elif(segment == "pointer"):
            index = str(int(index) + 3)
            writeFile.write("//Popping with Pointer\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@" + index + "\n")
            writeFile.write("M=D\n")
        elif(segment == "static"):
            writeFile.write("//Popping with Static\n")
            writeFile.write("@SP\n")
            writeFile.write("M=M-1\n")
            writeFile.write("A=M\n")
            writeFile.write("D=M\n")
            writeFile.write("@" + fileName[-8:periodIndex] + "." + index)
            writeFile.write("M=D\n")
#Start of Reading and Writing File
            
fileName = sys.argv[1]
readFile = open(fileName, 'r')
periodIndex = fileName.index(".")
writeFile = open(fileName[:periodIndex] + ".asm", "w")
for line in readFile:
    if line.strip() and (line[0:2] != "//"):
        print line
        currentCommand = commandType(line)
        if(currentCommand != "C_ARITHMETIC"):
            currentArg1 = arg1(line)
            currentArg2 = arg2(line)
            writePushPop(currentCommand, currentArg1, currentArg2)
            print currentArg1,currentArg2
        else:
            writeArithmetic(line)
        print currentCommand
readFile.close()
writeFile.close()
