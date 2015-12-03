import RPi.GPIO as io
io.setmode(io.BCM)
import sys, tty, termios, time
from termcolor import colored, cprint
 
motor1_in1_pin = 4
motor1_in2_pin = 17
io.setup(motor1_in1_pin, io.OUT)
io.setup(motor1_in2_pin, io.OUT)
 
motor2_in1_pin = 24
motor2_in2_pin = 25
io.setup(motor2_in1_pin, io.OUT)
io.setup(motor2_in2_pin, io.OUT)
 
 
io.setup(18, io.OUT)
io.output(18, False)
 
 
io.setup(23, io.OUT)
io.output(23, False)
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
def motor1_forward():
    io.output(motor1_in1_pin, True)
    io.output(motor1_in2_pin, False)
 
def motor1_reverse():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, True)
       
def motor1_stop():
    io.output(motor1_in1_pin, False)
    io.output(motor1_in2_pin, False)
 
def motor2_forward():
    io.output(motor2_in1_pin, True)
    io.output(motor2_in2_pin, False)
 
def motor2_reverse():
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, True)
 
def motor2_stop():
 
    io.output(motor2_in1_pin, False)
    io.output(motor2_in2_pin, False)
 
def toggleLights():
 
    global lightStatus
 
    if(lightStatus == False):
        io.output(18, True)
        io.output(23, True)
        lightStatus = True
    else:
        io.output(18, False)
        io.output(23, False)
        lightStatus = False
 
 
def toggleSteering(direction):
 
    global wheelStatus
 
    if(direction == "right"):
        if(wheelStatus == "centre"):
            motor1_forward()        
            wheelStatus = "right"
        elif(wheelStatus == "left"):
            motor1_stop()
            wheelStatus = "centre"
 
    if(direction == "left"):
        if(wheelStatus == "centre"):
            motor1_reverse()
            wheelStatus = "left"
        elif(wheelStatus == "right"):
            motor1_stop()
            wheelStatus = "centre"
 
 
io.output(motor1_in1_pin, False)
io.output(motor1_in2_pin, False)
io.output(motor2_in1_pin, False)
io.output(motor2_in2_pin, False)
 
lightStatus = False
wheelStatus = "centre"
 
 
bold = "\033[1m"
reset = "\033[0;0m"
cprint("Jacksons Awesome Rc car Program", 'blue')
print " " +bold + "w/s:" +reset + " acceleration"
print " " +bold + "a/d:" +reset + " steering"
print("l: lights")
print("x: exit now")
 
 
 
while True:
    char = getch()
    if(char == "w"):
        motor2_forward()
 
    if(char == "s"):
        motor2_reverse()
   
    if(char == "q"):
        motor2_stop()
     
    if(char == "d"):
        toggleSteering("left")
       
    if(char == "a"):
        toggleSteering("right")
 
    if(char == "l"):
        toggleLights()
   
    if(char == "o"):
        cPrint("hi", 'red')
 
    if(char == "x"):
        cprint("Program Ended", 'red')
        break
               
 
       
       
    char = ""
 
io.cleanup()