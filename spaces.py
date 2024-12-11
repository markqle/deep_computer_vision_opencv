import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photo/bear.jpeg')
cv.imshow('Bear', img)

#Color space: grayscale, RGB, HSV, YCrCb, etc., space of color, system to represent array of pixel color

#matplotlib: thing this is RGB instead of BGR
# plt.imshow(img)
# plt.show()

#BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

#BGR to HSV: hue, saturation, value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR', hsv_bgr)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)