import cv2 as cv
import numpy as np

img = cv.imread('photo/bear.jpeg')
cv.imshow('Bear', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
b,g,r = cv.split(img)

#blank set the color to black in the color components
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# this show lighter = intensity, black = no intensity
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)