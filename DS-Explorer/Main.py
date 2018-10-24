# * DS-Explorer is being developed for the TANGO Project: http://tango-project.eu
# * Copyright 2018 CETIC www.cetic.be
# * DS-Explorer is a free software: you can redistribute it and/or modify
# * it under the terms of the BSD 3-Clause License
# * Please see the License file for more information

# !/usr/bin/env python

import File_Parsing
import Report_parsing
import Command_Exec
import datetime

ts = str(datetime.datetime.now())  # Get timestamp and make it convert it to str type
ts = filter(str.isalnum, ts)  # Remove special characters from timestamp so that it can be used in folder name

sourcePath = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 32bits\impl\implementation_0"  # Location of the yaml files

a = File_Parsing.FileParse(sourcePath)

# Command line execution for compilation, build and implementation of design

b = Command_Exec.CommandExec(sourcePath)

# Location of reports generated after the design is implemented
reportsPath = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 32bits\implementations"
c = Report_parsing.ReportParse(reportsPath)
