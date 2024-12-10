import cv2 as cv

img = cv.imread('photo/bear.jpeg')

cv.imshow('Bear', img)

def rescaleFrame(frame, scale = 0.75):
    #Images, Vieos & Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def change_resolution(width, height):
    #Live video
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture('video/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
