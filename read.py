import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitkey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()