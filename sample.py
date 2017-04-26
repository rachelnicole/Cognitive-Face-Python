import cognitive_face as CF
import faces as face
from picamera import PiCamera 
from time import sleep
import subprocess


KEY = '06add3ffb377418fa5a4ed59d3d4325c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

img_url = '/home/pi/Desktop/image.jpg'
result = CF.face.detect(img_url)

while True:
  try:
    faceNumber = result[0][u'faceId']
    whoIsShe = CF.face.identify([ faceNumber ], 'my_anthem', 1)
    recognizedId = whoIsShe[0][u'candidates'][0][u'personId']
    if recognizedId == face.RACHEL:
      print "we found it!"
      print "It's Rachel"
      subprocess.call(['espeak "oh wow its rachel i cant believe it" 2>/dev/null'])
      subprocess.call(['aplay -fdat /home/pi/Desktop/Cognitive-Face-Python/rachel.wav'], shell=True)
      break
    elif recognizedId == face.TIERNEY:
      print "we found it!"
      subprocess.call(['es.say(are you ready for Twix)'])
      subprocess.call(['aplay -fdat /home/pi/Desktop/Cognitive-Face-Python/tierney.wav'], shell=True)
      break
    elif recognizedId == face.ANNIE:
      print "we found it!"
      subprocess.call(['es.say(Access granted welcome Annie)'])
      subprocess.call(['aplay -fdat /home/pi/Desktop/Cognitive-Face-Python/annie.wav'], shell=True)
      break
  except:
    subprocess.call(['espeak "oh no oh my this is awkward" 2>/dev/null'])
    subprocess.call(['aplay -fdat /home/pi/Desktop/Cognitive-Face-Python/unknown.wav'], shell=True)
    break


