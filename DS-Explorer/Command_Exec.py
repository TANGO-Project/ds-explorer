# * DS-Explorer is being developed for the TANGO Project: http://tango-project.eu
# * Copyright 2018 CETIC www.cetic.be
# * DS-Explorer is a free software: you can redistribute it and/or modify
# * it under the terms of the BSD 3-Clause License
# * Please see the License file for more information

import os


class CommandExec:
    def __init__(self, path):
        self.path = path
        pathfolder = path[:-17]
        folderList = os.listdir(pathfolder)
        fcount = 0
        folderList1 = []
        # Parse the directory to get the folders count
        for eachfolder in folderList:
            folderList1.append(eachfolder)
            fcount = fcount + 1
        config_counter = fcount - 1
        i = 0
        while i <= config_counter:
            comp = os.system("quickplay -cli compile --design=/home/lg/workspace/Clone_SobelPiP")
            build = os.system(
                "quickplay -cli build --design=/home/lg/workspace/Clone_SobelPiP --implementation=implementation_" + str(
                    i))
            impl = os.system(
                "quickplay -cli implement --design=/home/lg/workspace/Clone_SobelPiP --implementation=implementation_" + str(
                    i))
            i = i + 1
