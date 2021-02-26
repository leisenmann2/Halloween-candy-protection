import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

#detect faces for training recognition
def detect_face(img):
 img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 face_cascade = cv2.CascadeClassifier("/home/pi/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml")
 faces = face_cascade.detectMultiScale(img_gray,scaleFactor=1.2,minNeighbors=5)
 if (len(faces)==0):
  return None,None
 (x,y,w,h) = faces[0]
 return img_gray[y:y+w,x:x+h],faces[0]

#prepare training data
def prepare_training_data(data_folder_path):
 image_names = os.listdir(data_folder_path)
 faces=[]
 labels=[]
 for image_name in image_names:
  image_path = "data/Face_recog_data" + "/" + image_name
  image = cv2.imread(image_path)
  cv2.imshow("Training on :",image)
  plt.show()
  cv2.waitKey(100)
  face,rect = detect_face(image)
  if face is not None:
   faces.append(face)
   faces_resize = cv2.resize(faces[-1],(300,300)) #faces[0].shape + (50,50))
   faces[-1]=faces_resize
   labels.append(np.int(1))
   cv2.imshow(" ", faces[-1])
   plt.show()
   cv2.waitKey(100)  
  cv2.destroyAllWindows()
  cv2.waitKey(1)  
  cv2.destroyAllWindows()
 return faces,labels

#draw rectangle
def draw_rectangle(img,rect,color):
 (x,y,w,h) =rect
 if color == "green":
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
 elif color == "red":
  cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

#draw text
def draw_text(img,text,x,y,color):
 if color == "green":
  cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
 elif color == "red":
  cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2)

#recognize person
def predict(img1,image_shape,face_recognizer,subjects):
 img = img1.copy()
 face,rect = detect_face(img)
 if face is not None:
  faces_resize = cv2.resize(face,image_shape)
  label = face_recognizer.predict(faces_resize)
  print(label)
  if label[1]<40:
   label_text = subjects[label[0]] # + " " + str( np.round((100-label[1]),0)) + "%"
   draw_rectangle(img,rect,"green")
   draw_text(img,label_text,rect[0],rect[1]-5,"green")
   return img,True
  else:
   label_text = subjects[0]
   draw_rectangle(img,rect,"red")
   draw_text(img,label_text,rect[0],rect[1]-5,"red")
   return img,False
 else:
  #print("no face detected")
  return img,False
