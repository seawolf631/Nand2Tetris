import sys

#Reading & Writing File
for n in sys.argv[1:]:
    fileName = n
    readFile = open(fileName, "r")
    periodIndex = fileName.index(".")
    writeFile = open(fileName[:periodIndex] + "Ttest.xml", "a")

    writeFile.write("<tokens>")
    writeFile.write("</tokens>")

    readFile.close()
    writeFile.close()
