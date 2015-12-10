# UNIX2524 Introduction to UNIX
 
#### Project 3: MacFearCar300 In Python and Git
By: Bowei Zhao
Date: December 9, 2015
Class: ECE 2524 Introduction to UNIX Fall 2015

##INTRODUCTION
My Project for Unix will be of a Raspberry Pi Vehicle Robot running Python code. The idea in general is to create
a moving robotic vehicle from a completely self built and designed chassis to move at my will. 

##HOW TO
To run my project. You need a Raspberry Pi that is preferabbly the first generation Model B or past with 40pin GPIO.
You will also need the Raspberry Pi GPIO Python module that should come pre-installed on full images of Rasbian.
Root access is required to access GPIO on Raspberry Pi. Lastly, you will need Python 3.
No additional 3rd party modules are required to run this project if you have a Raspberry Pi with the GPIO library.

A sample command to running this project in the correct file directory would be:
sudo python block_car.py

Mine runs correctly without specifying Python version but yours may not. 

Be sure to quit the program by pressing X to successfully cleanup the GPIO pins so they don't remain active.

##SOFTWARE 
The MacFearCAR3000 or (MFC) for short will be developed on Raspbian Jessie which is a Linux distro based on Desbian and runs on ARM processors that the Raspberry Pi uses. This distro is the latest as of November 2015.

A development computer running Windows 8.1 and Ubuntu Linux 15.04 will be used to implement and write code onto the Pi. 

Python3 3.4.9 will be the version that the MFC will run off of. Do note that the RPi.GPIO Python Module is unique to run on the Raspberry Pi only and will not work on other systems without extensive modifications. The code can thus only be run and tested on a Raspberry Pi of at least Model B+ due to the GPIO pins the Python3 code is calling.

SSH will be the primary form of communication for running Python code on the Raspberry Pi, committing Github files, and controlling the vehicle as of this moment. Putty on Windows will be used mainly. 

SAMBA is the primary form of wireless network file/folder sharing as of right now between my desktop development computer and the Pi. SAMBA is licensed under GNU and is being used between Raspbian and Windows 8.1 or Ubuntu.

SFTP is the secondary form of wireless network file/folder sharing. WinSCP on Windows will be used mainly for this.

##HARDWARE
1: The project utilizes the Raspberry Pi 1 Model B as the base Linux computer the code runs off of.

2: An 16GB microSD card loaded with Raspbian Linux NOOBs

3: Robot Chassis w/ DC Motor and Wheel mount for DIY base

4: L293D Half Bridge Board for Pulse Width Modulation control of Motors

5: Extra Servo Motors, Sensors, Cables, and Mounts 

6: Two 5V, 1A rechargeable batteries to power Raspberry Pi and Motors

 
  
