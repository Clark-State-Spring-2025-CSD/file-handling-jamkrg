#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

echoFile = open("echo.txt")

curLine = echoFile.readline()
junk = echoFile.readline()
theRest = echoFile.read()

echoFile.close()

print(curLine)
print(theRest)