import os
import re
import shutil


class FileParse:
    def __init__(self, path):
        self.path = path
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
            # Go through each line of the yaml file. The line following the "property: width" line stores the value of
            # the width and thus it can be extracted.
            # Similarly the values of clock frequency & FIFO width can also be extracted.
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
                            retFreq = findValue1.group(1)
                # Parse and find FIFO width value
                prop2 = re.match("^\s*- property:\s*(.+)\s*$", line)
                if prop2:
                    prop2Is = prop2.group(1)
                    if 'size' in prop2Is:
                        value2 = currentFile.next()
                        findValue2 = re.match("^\s*value:\s*(.+)\s*$", value2)
                        if findValue2:
                            retFIFO = findValue2.group(1)  # type: str
                            # print("The FIFO size is %s in file: " % retFIFO + yamlList[i])
            i = i + 1
        print("The byte width is %s" % retWidth)
        print("The clock frequency is %s" % retFreq)
        print("The FIFO size is %s" % retFIFO)

        # Ask user if they want to change the config

        def change_config(destPath):
            # Ask the user if they want to change the values and give options for accepted values
            input1 = raw_input("Would you like to change the byte width?(Yes/No): ")
            input1 = input1.lower()
            if "yes" in input1:
                widthChanged = 1
                print("The byte width takes the following values: 8, 16, 32, 64")
                newWidth = raw_input("Enter the new byte width: ")
                while newWidth not in ['8', '16', '32', '64']:
                    print("Please select a value from the given options")
                    newWidth = raw_input("Enter the new byte width: ")
                width = newWidth
            else:
                width = retWidth
                widthChanged = 0
            input2 = raw_input("Would you like to change the clock frequency?(Yes/No): ")
            input2 = input2.lower()
            if "yes" in input2:
                freqChanged = 1
                print("The clock frequency takes the following values: 50, 75, 100, 200")
                newFreq = raw_input("Enter the new clock frequency: ")
                while newFreq not in ['50', '75', '100', '200']:
                    print("Please select a value from the given options")
                    newFreq = raw_input("Enter the new clock frequency: ")
                freq = newFreq
            else:
                freq = retFreq
                freqChanged = 0
            input3 = raw_input("Would you like to change the FIFO size?(Yes/No): ")
            input3 = input3.lower()
            if "yes" in input3:
                fifoChanged = 1
                print("The byte width takes the following values: 2048, 4096, 14400, 230400")
                newFifoSize = raw_input("Enter the new FIFO size: ")
                while newFifoSize not in ['2048', '4096', '14400', '230400']:
                    print("Please select a value from the given options")
                    newFifoSize = raw_input("Enter the new FIFO size: ")
                fifo = newFifoSize
            else:
                fifo = retFIFO
                fifoChanged = 0
            fileList1 = os.listdir(destPath)
            yamlList1 = []
            j = 0
            for everyFile in fileList1:
                if ".yaml" in everyFile:
                    yamlList1.append(everyFile)
            if widthChanged or freqChanged or fifoChanged:
                for eachfile1 in yamlList1:
                    yamlFile1 = destPath + '\\' + yamlList1[j]
                    curfile = open(yamlFile1, 'r')
                    lines = curfile.readlines()
                    curfile.close()
                    a = 'value: ' + retWidth
                    b = 'value: ' + retFreq
                    c = 'value: ' + retFIFO
                    curfile = open(yamlFile1, 'w')
                    for eachline1 in lines:
                        if a in eachline1:
                            eachline1 = '\t  value: ' + width + '\n'
                        if b in eachline1:
                            eachline1 = '\t  value: ' + freq + '\n'
                        if c in eachline1:
                            eachline1 = '\t  value: ' + fifo + '\n'
                        curfile.write(eachline1)
                    curfile.close()
                    j = j + 1

        # Ask user if they want to change config for the first time
        input0 = raw_input("Do you want to change the config?(Yes/No): ")
        input0 = input0.lower()
        pathfolder = path[:-17]
        folderList = os.listdir(pathfolder)
        fcount = 0
        folderList1 = []
        # Parse the directory to get the folders count
        for eachfolder in folderList:
            folderList1.append(eachfolder)
            fcount = fcount + 1
        config_counter = fcount - 1
        if "yes" in input0:
            config_counter = config_counter + 1
            destPath = self.path[:-1] + str(config_counter)
            shutil.copytree(self.path, destPath, symlinks=False, ignore=None)
            change_config(destPath)
            # Ask if user wants to test more variations of configs
            input_config = raw_input("Do you want to test another config?(Yes/No): ")
            input_config = input_config.lower()
            while "yes" in input_config:
                config_counter = config_counter + 1
                destPath = self.path[:-1] + str(config_counter)
                shutil.copytree(self.path, destPath, symlinks=False, ignore=None)
                change_config(destPath)
                input_config = raw_input("Do you want to test another config?(Yes/No): ")
                input_config = input_config.lower()


