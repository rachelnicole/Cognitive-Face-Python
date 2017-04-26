import cognitive_face as CF
import faces as face
from picamera import PiCamera 
from time import sleep


KEY = '06add3ffb377418fa5a4ed59d3d4325c'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

camera = PiCamera()

camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()



img_url = '/home/pi/Desktop/image.jpg'
result = CF.face.detect(img_url)

faceNumber = result[0][u'faceId']

# This compares our known faceId to our group
whoIsShe = CF.face.identify([ faceNumber ], 'my_anthem', 1)

recognizedId = whoIsShe[0][u'candidates'][0][u'personId']

print '-----------------'

print whoIsShe[0][u'candidates'][0][u'personId']

if recognizedId == face.RACHEL:
  print "we found it!"
  print "It's Rachel"
  subprocess.call(['aplay -fdat meow.wav'], shell=True)
elif recognizedId == face.TIERNEY:
  print "we found it!"
  print "It's Tierney!"
elif recognizedId == face.ANNIE:
  print "we found it!"
  print "It's Annie!"
else:
   print "I don't know her"

