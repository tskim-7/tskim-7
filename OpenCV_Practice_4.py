import cv2

img_src = "dog.png"
img_dst = "dog_result.png"

img = cv2.imread(img_src, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow('title', img)
    cv2.imwrite(img_dst, img)
else:
    print("이미지가 정상적으로 불러오지 않았습니다")    

cv2.waitKey()
cv2.destroyAllWindows()