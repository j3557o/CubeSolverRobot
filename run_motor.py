import sys
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

def rotate_one_motor(motor, angle):
    print("Rotate")

def rotate_two_motors(motor1, motor2, angle):
    print("Rotate 2")

def calibrate_motor(motor, stop_pin):
    print("Calibrate " + str(motor))