#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2


# In[2]:


#load cascade classifier
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")


# In[3]:


# Load the Cascade Classifier
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")
 
#startt  web cam
cap = cv2.VideoCapture(r"C:\Users\RAM\Downloads\video.mp4")
 
while True:
     
    #time.sleep(0.2)
     
    #read image from webcam
    respose, color_img = cap.read()
     
    if respose == False:
        break
     
    # Convert to grayscale
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
     
    # Detect the faces
    faces = car_cascade.detectMultiScale(gray_img, 1.1, 1)
     
    #display rectrangle
    i=0
    for (x, y, w, h) in faces:
        if i%2==0:
            cv2.rectangle(color_img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            i +=1
        else:
            cv2.rectangle(color_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            i +=1      
     
        # display image
        cv2.imshow('Vehicle detection', color_img)
             
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
 # Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()


# In[ ]:




