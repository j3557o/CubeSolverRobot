import io
import img_proc
import grab_image



cube_side = grab_image.grab_image()
cube_string = img_proc.list_colors(cube_side)
print(cube_string)