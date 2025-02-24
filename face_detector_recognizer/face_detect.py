import cv2 as cv

img = cv.imread('photo/boo_bear.jpeg')
cv.imshow('face', img)

#haar cascade use the edge detector to detect faces
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Detect faces, minNeighbors: how many neighbors to check for every potential object, make it susceptible to noise
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
print(f'Number of faces found = {len(faces_rect)}')

# Draw rectangles around faces
for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Detected Faces', img)


capture = cv.VideoCapture('video/pickleball.mov')

while True:
    isTrue, frame = capture.read()
    # cv.imshow('Video', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('Grayscale', gray)

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    print(f'Number of faces found = {len(faces_rect)}')

    # Draw rectangles around faces
    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('Detected Faces', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)
# cv.destroyAllWindows()