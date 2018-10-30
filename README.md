# DS-Explorer

&copy; CETIC 2018 www.cetic.be

DS-Explorer is currently developed as a component within the framework of [TANGO](http://tango-project.eu) European Project

DS-Explorer is distributed under a [BSD 3-Clause License](https://github.com/TANGO-Project/ds-explorer/blob/master/LICENSE).

## Description

The DS-Explorer tool is intended for design space exploration at a higher level. DS-Explorer aims at easing the exploration of design space alternatives when FPGA acceleration is involved.

## Installation

DS-Explorer, is written in Python, and supported on standard Linux distributions.
While it was first intended to interface with various HLS (High Level Synthesis) tools, we focused, for the first release, on leveraging
QuickPlay  which provides support for various FPGA targets and generates the low-level hardware and communication interfaces with the
FPGA.
To install the QuickPlay IDE, the user should refer to the installation instructions here (account needed):
https://quickstore.quickplay.io/content/quickplay-software
To install DS-Explorer, a user just needs to copy the program files into a folder of his choice and optionally add that folder to the user’s system path to allow seamless execution of the program.

## Platforms Supported

DS-Explorer is developed using Python 2.7 and therefore supported on standard Linux platforms and recent OS X and MS Windows systems.
However, DS-Explorer needs a baseline QuickPlay project that must be generated by the QuickPlay tool suite.
QuickPlay is supported on RHEL7 (Red Hat Enterprise Linux 7 OS): this is currently the only supported platform for the QuickPlay IDE. It requires a minimum of 10GB of RAM.
DS-Explorer and QuickPlay can be located on different machines. However, this may involve several manual operations in copying files between the two systems.
Another option consists of using a RHEL7 virtual machine and installing both DS-Explorer and QuickPlay on it. The VM could then be run on any system supporting virtualisation.

The target platforms are FPGA PCI based accelerator boards for which the low-level support is provided seamlessly by the QuickPlay backend. The user can select (and switch) between the various targets available in the QuickPlay environment. The list of currently supported platforms includes several boards with Xilinx Kintex-7 and Kintex UltraScale FPGA references, as well as Intel/Altera Arria-10 and Stratic V FPGA references also. Currently supported boards are listed in Figure 4. Further details on the boards are available at this link (requires login):
 https://quickstore.quickplay.io/catalog/boards

Access to some of these FPGA platforms is enabled through cloud services from providers like Amazon and OVH labs and fully integrated in the QuickPlay IDE. Additionally, it is possible to target the same FPGA boards if they are hosted locally

## Software Pre-requisites and Dependencies
Dependency	Version	Comment
Python 	2.7	DS-Explorer is written in Python
Red Hat Enterprise Linux 	7	Requirement of the underlying tool QuickPlay

## Installation Instructions
As previously indicated, DS-Explorer, being written in Python, only needs that the Python environment be available on the development machine (or virtual machine) and the DS-Explorer source files tree be copied locally.

## Example of Tool Usage
The tool is run, passing the paths of the project argument:

``$ ./DS-Explorer.py QuickPlay/MyProject/``

The number of yaml files is counted and displayed to the user along with the byte width, frequency and FIFO size

```output
Number of yaml files = 14

The byte width is 8

The clock frequency is 50

The FIFO size is 14400````

The user is prompted for changing the configuration
```` 
Do you want to change the config?(Yes/No): yes

Would you like to change the byte width?(Yes/No): yes

The byte width takes the following values: 8, 16, 32, 64

Enter the new byte width: 16

Would you like to change the clock frequency?(Yes/No): no

Would you like to change the FIFO size?(Yes/No): yes

The byte width takes the following values: 2048, 4096, 14400, 230400

Enter the new FIFO size: 4096

Do you want to test another config?(Yes/No): yes

Would you like to change the byte width?(Yes/No): no

Would you like to change the clock frequency?(Yes/No): yes

The clock frequency takes the following values: 50, 75, 100, 200

Enter the new clock frequency: 100

Would you like to change the FIFO size?(Yes/No): no

Do you want to test another config?(Yes/No): no````

When the user has completed assigning the different configurations, the different configs will be compiled and implemented and the reports generated.
````
INFO-01:    ===================================================================

INFO-01:    QuickPlay batch version: 4.1.6

INFO-01:    Mode      : client

INFO-01:    Step      : compile

INFO-01:    Project   : Clone_SobelPiP

INFO-01:    Solution  : implementation_0

INFO-01:    Start time: 26/Oct/2018-11:19:50 UTC

INFO-01:    ===================================================================

INFO-01:    Starting project Clone_SobelPiP compile step ...

INFO-01:    Starting project check...  

INFO-01:    Project check successfully done.

INFO-01:    Starting C++ compilation...
.
.
.
.
.
INFO-01:    Project MyProject implement step for implementation_0 successfully done.
INFO-01:    ===================================================================
INFO-01:    End time  : 14/Aug/2018-11:10:30 UTC ( elapsed: 3128.879 secs)
INFO-01:    Exit value: 0
INFO-01:    ===================================================================

````
A consolidated report is generated in the root folder, after parsing through the reports obtained from QuickPlay implementation.

**Example of the generated file:**
> CLB Logic Distribution
>
> | Site Type | Used     | Fixed | Available | Util% |
> |:----------|:---------|:----------|:---------|
> | CLB                                       | 10293 |     0 |     30300 | 33.97 |
> | LUT as Logic                              | 51630 |     0 |    242400 | 21.30 |
> | LUT as Memory                             |   470 |     0 |    112800 |  0.42 |
> | LUT Flip Flop Pairs                       | 24930 |     0 |    242400 | 10.28 |

>
> BLOCKRAM
>
> |     Site Type     | Used | Fixed | Available | Util%  |
> | :------------- | :------------- |
> |Block RAM Tile    |  222 |     0 |       600 | 37.00 |
> |   RAMB36/FIFO*    |  192 |     2 |       600 | 32.00 |
> |   RAMB18          |   60 |    12 |      1200 |  5.00 |
>
> Arithmetic
>
> | Site Type | Used | Fixed | Available | Util% |
> | :------------- | :------------- |
> |DSPs      |    0 |     0 |      1920 |  0.00
>
> Advanced
>
> | Site Type    | Used | Fixed | Available | Util% |
> | :------------- | :------------- |
> | PCIE_3_1        |    1 |     1 |         3 | 33.33
>
> Clock Primitive Utilization
>
> |  Type       | Used | Available | LOC | Clock Region | Pblock |
> | :------------- | :------------- |
> | BUFGCE     |    8 |       240 |   0 |            0 |      0 |
> | BUFGCE_DIV |    0 |        40 |   0 |            0 |      0 |
> | BUFGCTRL   |    0 |        80 |   0 |            0 |      0 |
> | BUFG_GT    |    5 |       120 |   0 |            0 |      5 |
> | MMCM       |    1 |        10 |   0 |            0 |      0 |
> | PLL        |    0 |        20 |   0 |            0 |      0 |
>
> Total Power and Dynamic Power
>
> | Power   | Value     |
> | :------------- | :------------- |
> |  Total On-Chip Power (W)  | 3.592  |
> | Dynamic (W)              | 3.035    |
