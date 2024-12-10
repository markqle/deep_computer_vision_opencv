import cv2 as cv

# img = cv.imread('photo/bear.jpeg')

# cv.imshow('Bear', img)

capture = cv.VideoCapture('video/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
