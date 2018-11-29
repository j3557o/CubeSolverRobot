import io
import img_proc
import grab_image
import solver as sv


#cube_side = grab_image.grab_image()
#cube_string = img_proc.list_colors(cube_side)
#Turn cube and loop

cube_string = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
a = sv.solve(cube_string, 20, 2)
print(cube_string)
print(a)

#Solve
