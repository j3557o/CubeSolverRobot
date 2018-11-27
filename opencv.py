from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.resolution = (3280,2464)
camera.start_preview()
sleep(1)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()