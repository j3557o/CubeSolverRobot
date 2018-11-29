#Grab image from PiCamera, returns an io_stream object

import io
from picamera import PiCamera
#from PIL import Image
from time import sleep


def grab_image():
    io_stream = io.BytesIO()
    camera = PiCamera()
    camera.resolution = (3280,2464)
    print("#Turn on LED")
    camera.start_preview()
    sleep(2)
    camera.capture(io_stream, 'jpeg')
    camera.stop_preview()
    print("#Turn off LED")
    io_stream.seek(0)
    return io_stream
    