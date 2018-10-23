import File_Parsing
import Report_parsing
import Command_Exec
import datetime

ts = str(datetime.datetime.now())      # Get timestamp and make it convert it to str type
ts = filter(str.isalnum, ts)           # Remove special characters from timestamp so that it can be used in folder name

sourcePath = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 32bits\impl\implementation_0"     # Location of the yaml files

a = File_Parsing.FileParse(sourcePath)

# Command line execution for compilation, build and implementation of design

b = Command_Exec.CommandExec(sourcePath)

# Location of reports generated after the design is implemented
reportsPath = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 32bits\implementations"
c = Report_parsing.ReportParse(reportsPath)
