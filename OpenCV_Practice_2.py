# pip install opencv-python
# pip install opencv-contrib-python

import cv2

img_src = "dog.png"
img = cv2.imread(img_src)

cv2.imshow('title', img)
cv2.waitKey()
cv2.destroyAllWindows()