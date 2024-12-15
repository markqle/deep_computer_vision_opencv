import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')
people = []
for i in os.listdir(r'./faces/train'):
    if i != '.DS_Store':
        people.append(i)
DIR = r'./faces/train'

# features = np.load('feature.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'./faces/val/taylorswift/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)


#Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.4, 3)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label: {people[label]} with confidence: {confidence}')

    cv.putText(img, str(people[label]), (img.shape[1]//2, img.shape[0]//2), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)