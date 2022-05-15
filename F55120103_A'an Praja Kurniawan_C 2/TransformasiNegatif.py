import cv2

img = cv2.imread("img/aan.jpg", 0)

img_1 = 255 - img

cv2.imshow("Gambar Hesti Original", img)
cv2.imshow("Gambar Hesti Negative", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()