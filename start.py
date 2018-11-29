#!/usr/bin/python3
#Start this script

import io
import img_proc
import grab_image
import solver as sv
import run_motor

MotorA_pins = [22,27,17,4]
MotorB_pins = [22,27,17,4]
MotorC_pins = [22,27,17,4]
MotorD_pins = [22,27,17,4]
Grabber_motor_pins = [22,27,17,4]

#Calibration routine
#run_motor.calibrate(Grabber_motor_pins, 5)
#run_motor(MotorA_pins, 6)
#run_motor(MotorB_pins, 7)
#run_motor(MotorC_pins, 8)
#run_motor(MotorD_pins, 9)


#Open grabbers
#Wait for input key

#Close grabbers



cube_side = grab_image.grab_image()
cube_string = img_proc.list_colors(cube_side)
#Turn cube and loop

cube_string = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
cube_solve_string = sv.solve(cube_string, 20, 2)
print(cube_string)
print(cube_solve_string)

#Solve
#Create look up table Mapping D L U R B F to motor1, motor2, motor3, motor4, up or down
#If side to turn is mapped to up or down
#Do rotate_cube and update table
#Rotate_side
#Loop through cube_solve_string
