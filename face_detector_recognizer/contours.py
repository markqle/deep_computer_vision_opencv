import cv2 as cv
import numpy as np

img = cv.imread('photo/bear.jpeg')

cv.imshow('Bear', img)
#Contour: line / curve of objects, join the continuous points of an object
#Math: contour: shape analysis & object recognition


blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grayscale', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)
#Grab the edge
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#Chain approx 
    #+ SIMPLE: -> make it into 1 line, 2 end points
    #+ NONE -> no end points, all the points are stored
#retr_list = all contour in the image
#retr_external = all outside contour
#retr_tree = contour hierarchy

ret, thresh = cv.threshold(canny, 125,255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)