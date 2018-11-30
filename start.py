#!/usr/bin/python3
#Start this script

import threading
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
t1 = threading.Thread(target=run_motor.calibrate_motor(Grabber_motor_pins, 5))
t2 = threading.Thread(target=run_motor.calibrate_motor(MotorA_pins, 6))
t3 = threading.Thread(target=run_motor.calibrate_motor(MotorB_pins, 7))
t4 = threading.Thread(target=run_motor.calibrate_motor(MotorC_pins, 8))
t5 = threading.Thread(target=run_motor.calibrate_motor(MotorD_pins, 9))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()

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
