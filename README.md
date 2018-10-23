# DS-Explorer

&copy; CETIC 2018 www.cetic.be

DS_Explorer is currently developed as a component within the framework of [TANGO](http://tango-project.eu) European Project

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

Current version of DS-Explorer is a command line tool that realizes the following steps:
1.	DS-Explorer parses the configuration files of the QuickPlay project that is passed as a parameter and extracts the relevant
configuration parameters that can be tuned, modified or adapted to explore various derivatives from the original design.
2.	DS-Explorer exposes those parameters to the user and asks them about the variations they would like to explore through a series
of questions and answers (Q&A).
3.	Based on the user answers, DS-Explorer generates clones of the original design with the new parameters as specified by the user
4.	DS-Explorer compile, builds and implements the different generated QuickPlay designs. This will produce various reports, of which
the power, timing and resource utilization reports are the most important
5.	DS-Explorer parses output reports and formats relevant characterization data about power, timing and resource utilization for the
different implementations of the FPGA kernel in a raw output file. These data will serve as attribute values in the JSON input file for
the Placer tool. Future versions of DS-Explorer will handle automatic generation of JSON file generation.
