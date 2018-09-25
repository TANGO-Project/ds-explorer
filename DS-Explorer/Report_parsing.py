#!/bin/python

###############################################################################################

path = "C:\RH7_Shared\Clone_SobelPiP_50Mhz & 8 bits\implementations\implementation_0\\reports"  # Location of reports

with open(path + "\utilization.rpt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

clbLogicDistribution = 0
blockRam = 0
arithmetic = 0
advanced = 0
file_rpt = open("Consolidated_Report.txt", 'w')        # Create text file if file doesn't exist
for line in content:
    if "CLB Logic Distribution" in line:
        clbLogicDistribution += 1
        if clbLogicDistribution == 2:
            line = line.strip('2. ')
            file_rpt.write('\n' + line)
    if "BLOCKRAM" in line:
        blockRam += 1
        if blockRam == 2:
            line = line.strip('3. ')
            file_rpt.write('\n' + line)
    if "ARITHMETIC" in line:
        arithmetic += 1
        if arithmetic == 2:
            line = line.strip('4. ')
            file_rpt.write('\n' + line)
    if "ADVANCED" in line:
        advanced += 1
        if advanced == 2:
            line = line.strip('7. ')
            file_rpt.write('\n' + line)
    if clbLogicDistribution == 2:
        if "| CLB" in line:
            file_rpt.write('\n' + "+-------------------------------------------+-------+-------+-----------+-------+")
            file_rpt.write('\n' + "|                 Site Type                 |  Used | Fixed | Available | Util% |")
            file_rpt.write('\n' + "+-------------------------------------------+-------+-------+-----------+-------+")
            file_rpt.write('\n' + line)
        if "| LUT as Logic" in line:
            file_rpt.write('\n' + line)
        if "| LUT as Memory" in line:
            file_rpt.write('\n' + line)
        if "| LUT Flip Flop Pairs" in line:
            file_rpt.write('\n' + line)
            file_rpt.write("\n+-------------------------------------------+-------+-------+-----------+-------+")
            clbLogicDistribution = 0

    if blockRam == 2:
        if "| Block RAM Tile" in line:
            file_rpt.write("\n+-------------------+------+-------+-----------+-------+")
            file_rpt.write("\n|     Site Type     | Used | Fixed | Available | Util% |")
            file_rpt.write("\n+-------------------+------+-------+-----------+-------+")
            file_rpt.write('\n' + line)
        if "|   RAMB36/FIFO" in line:
            file_rpt.write('\n' + line)
        if "|   RAMB18" in line:
            file_rpt.write('\n' + line)
            file_rpt.write("\n+-------------------+------+-------+-----------+-------+")
            blockRam = 0

    if arithmetic == 2:
        if "DSPs" in line:
            file_rpt.write("\n+-----------+------+-------+-----------+-------+")
            file_rpt.write("\n| Site Type | Used | Fixed | Available | Util% |")
            file_rpt.write("\n+-----------+------+-------+-----------+-------+")
            file_rpt.write('\n' + line)
            file_rpt.write("\n+-----------+------+-------+-----------+-------+")
            arithmetic = 0

    if advanced == 2:
        if "| PCIE" in line:
            file_rpt.write("\n+-----------------+------+-------+-----------+-------+")
            file_rpt.write("\n|    Site Type    | Used | Fixed | Available | Util% |")
            file_rpt.write("\n+-----------------+------+-------+-----------+-------+")
            file_rpt.write('\n' + line)
            file_rpt.write("\n+-----------------+------+-------+-----------+-------+")
            advanced = 0

###############################################################################################
with open(path + "\clock_utilization.rpt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

clockPrimitiveUtilization = 0

for line in content:
    if "Clock Primitive Utilization" in line:
        clockPrimitiveUtilization += 1
        if clockPrimitiveUtilization == 2:
            line = line.strip('1. ')
            file_rpt.write('\n' + line)
    if clockPrimitiveUtilization == 2:
        if "| BUFGCE     |" in line:
            file_rpt.write("\n+------------+------+-----------+-----+--------------+--------+")
            file_rpt.write("\n| Type       | Used | Available | LOC | Clock Region | Pblock |")
            file_rpt.write("\n+------------+------+-----------+-----+--------------+--------+")
            file_rpt.write('\n' + line)
        if "| BUFGCE_DIV |" in line:
            file_rpt.write('\n' + line)
        if "| BUFGCTRL   |" in line:
            file_rpt.write('\n' + line)
        if "| BUFG_GT    |" in line:
            file_rpt.write('\n' + line)
        if "| MMCM       |" in line:
            file_rpt.write('\n' + line)
        if "| PLL        |" in line:
            file_rpt.write('\n' + line)
            file_rpt.write("\n+------------+------+-----------+-----+--------------+--------+")
            clockPrimitiveUtilization = 0

###############################################################################################
with open(path + "\power.rpt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

summary = 0

for line in content:
    if "1. Summary" in line:
        summary += 1
        if summary == 2:
            file_rpt.write("\nTotal power and dynamic power")
            file_rpt.write("\n+--------------------------+--------+")

    if summary == 2:
        if "| Total On-Chip Power (W)  |" in line:
            file_rpt.write('\n' + line)
        if "| Dynamic (W)              |" in line:
            file_rpt.write('\n' + line)
            file_rpt.write("\n+--------------------------+--------+")
            summary = 0
print("\nConsolidated report file generated\n")