# UNIX2524
Introduction to UNIX
 
 -- Project 3: Python and Git and Linux

### MacFearCAR3000

#INTRODUCTION
My Project for Unix will be of a Raspberry Pi Vehicle Robot running Python code. The idea in general is to create
a moving robotic vehicle from a completely self built and designed chassis to move at my will. 

#SOFTWARE 
The MacFearCAR3000 or (MFC) for short will be developed on Raspbian Jessie which is a Linux distro based on Desbian and runs on ARM processors that the Raspberry Pi uses. This distro is the latest as of November 2015.

A development computer running Windows 8.1 and Ubuntu Linux 15.04 will be used to implement and write code onto the Pi. 

Python3 3.4.9 will be the version that the MFC will run off of. Do note that the RPi.GPIO Python Module is unique to run on the Raspberry Pi only and will not work on other systems without extensive modifications. The code can thus only be run and tested on a Raspberry Pi of at least Model B+ due to the GPIO pins the Python3 code is calling.

SSH will be the primary form of communication for running Python code on the Raspberry Pi, committing Github files, and controlling the vehicle as of this moment. Putty on Windows will be used mainly. 

SAMBA is the primary form of wireless network file/folder sharing as of right now between my desktop development computer and the Pi. SAMBA is licensed under GNU and is being used between Raspbian and Windows 8.1 or Ubuntu.

SFTP is the secondary form of wireless network file/folder sharing. WinSCP on Windows will be used mainly for this.
 
