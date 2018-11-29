#!/usr/bin/python3
#Start this script

import io
import img_proc
#import grab_image
import solver as sv

#Calibration routine

#Open grabbers
#Wait for input key



#cube_side = grab_image.grab_image()
#cube_string = img_proc.list_colors(cube_side)
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
