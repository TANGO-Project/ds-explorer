#!/usr/bin/env python

# * DS-Explorer is being developed for the TANGO Project: http://tango-project.eu
# * Copyright 2018 CETIC www.cetic.be
# * DS-Explorer is a free software: you can redistribute it and/or modify
# * it under the terms of the BSD 3-Clause License
# * Please see the License file for more information


import sys
import File_Parsing
import Report_parsing
import Command_Exec

sourcePath = sys.argv[1]  # Location of the yaml files

a = File_Parsing.FileParse(sourcePath)

# Command line execution for compilation, build and implementation of design

b = Command_Exec.CommandExec(sourcePath)

# Report parsing and generation of consolidated report after implementation

c = Report_parsing.ReportParse(sourcePath)
