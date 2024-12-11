import cv2 as cv
import numpy as np
img = cv.imread('photo/bear.jpeg')

cv.imshow('Bear', img)

#Translation - shift image along x, y axis
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#Rotation - rotate image with an angle
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_roated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_roated)


#Resize an image
resized = cv.resize(img, (500, 500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flip an image
flip = cv.flip(img, -1)
cv.imshow('Flipped', flip)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)