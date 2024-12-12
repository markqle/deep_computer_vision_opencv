import cv2 as cv

img = cv.imread('photo/bear.jpeg')
cv.imshow('Bear', img)

#thresholding: binary realization of the image
#Take image, take value of threshold, compare pixel with threshold, if less = 0, more = 1. Then we can create a binary image
# Simple thresholding & Adaptive thresholding

#SIMPLE THRESHOLD
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#Threshold value, threshold image
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold Binary', thresh)

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Binary Inverse', thresh_inverse)


#ADAPTIVE THRESHOLD - let computer decide the threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('Adaptive Threshold Binary', adaptive_thresh)


cv.waitKey(0)