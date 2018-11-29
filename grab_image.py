import io
from picamera import PiCamera
from time import sleep


def grab_image():
    camera = PiCamera()
    camera.resolution = (3280,2464)
    camera.start_preview()
    sleep(2)
    camera.capture(io_stream, 'jpeg')
    camera.stop_preview()
    io_stream.seek(0)
    return Image.open(io_stream)
    