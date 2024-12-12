#smooth the image it tends to have a lot of noise due to camera sensor
import cv2 as cv

img = cv.imread('photo/bear.jpeg')
cv.imshow('Bear', img)

#define kernel, kernel size = number of columns and rows in a window over the portion of the image

#Averaging, define kernel, it compute the pixel intensity of the middle pixel as the average of the pixel intensities in the neighborhood. -> this happens throughout the image

average = cv.blur(img, (3,3))
cv.imshow('Average', average)


#Gausian blur, each neighborhood pixel has a different weight, the average product of those weights is used to compute the new pixel intensity of the center piece. (More natural blur)
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss)

#Median blur, instead of taking the average, it replaces each pixel with the median value of all the pixels in the neighborhood. (Most reduce noise)
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#Bilateral blur, reducing the edges of the image
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)