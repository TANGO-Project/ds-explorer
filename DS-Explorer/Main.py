import shutil
import File_Parsing
import Report_parsing
import datetime
import os

ts = str(datetime.datetime.now())      # Get timestamp and make it convert it to str type
ts = filter(str.isalnum, ts)           # Remove special characters from timestamp so that it can be used in folder name

sourcePath = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 8 bits\impl\implementation_0"     # Location of the yaml files
destPath = "C:/Users/bv/Documents/backup_yaml/" + ts                                 # Location to store backup files
shutil.copytree(sourcePath, destPath, symlinks=False, ignore=None)
print("Files backed up\n")

a = File_Parsing.FileParse(sourcePath)

# Command line execution for compilation, build and implementation of design

comp = os.system("quickplay -cli compile --design=/home/lg/workspace/Clone_SobelPiP")
build = os.system("quickplay -cli build --design=/home/lg/workspace/Clone_SobelPiP --implemntation=implementation_0")
impl = os.system("quickplay -cli implement --design=/home/lg/workspace/Clone_SobelPiP --implemntation=implementation_0")

# Location of reports generated after the design is implemented
reportsPath = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 8 bits\implementations\implementation_0\\reports"
b = Report_parsing.ReportParse(reportsPath)
