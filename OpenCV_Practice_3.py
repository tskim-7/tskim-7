import cv2

img_src = "dog.png" 
img1 = cv2.imread(img_src, 1)
img2 = cv2.imread(img_src, 0)
img3 = cv2.imread(img_src, -1)


#cv2.IMREAD_COLOR 1
#cv2.IMREAD_GRAYSCALE 0
#cv2.UNCHANGED -1

cv2.imshow('title', img1)
cv2.imshow('title2', img2)
cv2.imshow('title3', img3)

cv2.waitKey()
cv2.destroyAllWindows()