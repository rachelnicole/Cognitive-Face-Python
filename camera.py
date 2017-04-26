import io, os, sys, requests

from PIL import Image
from picamera import PiCamera
from time import sleep

_maxNumRetries = 10

camera = PiCamera()


camera.rotation = 270
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

json = None

data = open('/home/pi/Desktop/image.jpg', 'rb').read()