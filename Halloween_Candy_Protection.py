from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep
import cv2
from face_recog_final import *
import light
import Servo as sv

#init camera
camera = PiCamera()
camera.resolution =(640,480)
camera.framerate = 42
rawCapture = PiRGBArray(camera,size=(640,480))

#warmup
sleep(0.1)

#make sure servo is on close
sv.setup()
#sv.close()
#sv.destroy()

#turn on the red light
light.setup()
light.setColor(0,100)

#set detected parameter to False
detected = False

#initialize face recognition
print("preparing data...")
faces,labels= prepare_training_data("data/Face_recog_data")
print("Done")
print("Faces: ", len(faces))
image_shape = (300,300) 
subjects=["unknown ", "Lukas Eisenmann"]

#Train Face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces,np.array(labels))

#save to video
video = cv2.VideoWriter("video.avi",0,12,(640,480))

#capture frames
for frame in camera.capture_continuous(rawCapture,format="bgr", use_video_port=True):
 #capture frame
 image = frame.array

 #predict faces 
 predict1,detected = predict(image,image_shape,face_recognizer,subjects)

 #if i am detected open box and turn on green light
 if detected == True:
 # cv2.imshow("img",predict1)
  #sleep(2)
  light.setColor(100,0)
  sv.open() 
  sv.destroy()

 #show frame
 cv2.imshow("img",predict1)
 video.write(predict1)
 key = cv2.waitKey(1) & 0xFF

 #save to video
# video.write(predict1) 

 #clear stream
 rawCapture.truncate(0)

 #exit loop
 if key == ord("q"):
  break

video.release()
camera.close()
light.destroy()
sv.destroy()
