import os
import re

path = "C:\RH7_Shared\Clone_SobelPiP_50MHz & 8 bits\impl\implementation_0"  # Location of the yaml files
fileList = os.listdir(path)
count = 0
yamlList = []
i = 0

# Parse the directory to get the yaml files count
for eachFile in fileList:
    if ".yaml" in eachFile:
        yamlList.append(eachFile)
        count = count + 1
print {"Number of yaml files = %d" % count}
# Parse each file and extract byte width, clock frequency & FIFO width and display the values to the user
for each in yamlList:
    yamlFile = path + '\\' + yamlList[i]
    currentFile = open(yamlFile)
# Go through each line of the yaml file. The line following the "property: width" line stores the value of the width
# and thus it can be extracted. Similarly the values of clock frequency & FIFO width can also be extracted.
    for line in currentFile:
        prop = re.match("^\s*- property:\s*(.+)\s*$", line)
        if prop:
            propIs = prop.group(1)
            if 'width' in propIs:
                value = currentFile.next()
                findValue = re.match("^\s*value:\s*(.+)\s*$", value)
                if findValue:
                    retWidth = findValue.group(1)
    # Parse and find clock frequency value
        prop1 = re.match("^\s*- property:\s*(.+)\s*$", line)
        if prop1:
            prop1Is = prop1.group(1)
            if 'clockFrequency' in prop1Is:
                value1 = currentFile.next()
                findValue1 = re.match("^\s*value:\s*(.+)\s*$", value1)
                if findValue1:
                    retClock = findValue1.group(1)
    # Parse and find FIFO width value
        prop2 = re.match("^\s*- property:\s*(.+)\s*$", line)
        if prop2:
            prop2Is = prop2.group(1)
            if 'size' in prop2Is:
                value2 = currentFile.next()
                findValue2 = re.match("^\s*value:\s*(.+)\s*$", value2)
                if findValue2:
                    retFIFO = findValue2.group(1)
#                    print("The FIFO size is %s in file: " % retFIFO + yamlList[i])
    i = i + 1
print("The byte width is %s" % retWidth)
print("The clock frequency is %s" % retClock)
print("The FIFO size is %s" % retFIFO)
# Ask the user if they want to change the values and give options for accepted values
ip1 = input("Would you like to change the byte width?(Yes/No): ")
if 'y' or 'Y' in ip1:
    print("The byte width takes the following values: 8, 16, 32, 64")
    newWidth = input("Enter the new byte width: ")
# input2 = input("Would you like to change the clock frequency?(y/n)")
# if input2 is "y":
#     print("The clock frequency takes the following values: 50, 75, 100, 200")
#     newFreq = input("Enter the new clock frequency: ")
# input3 = input("Would you like to change the FIFO size?(y/n)")
# if input3 is "y":
#     print("The byte width takes the following values: 2048, 4096, 14400, 230400")
#     newFifoSize = input("Enter the new FIFO size: ")

