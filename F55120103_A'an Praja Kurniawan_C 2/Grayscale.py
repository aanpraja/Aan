import cv2

img = cv2.imread("img/aan.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Hesti Original", img)
cv2.imshow("Gambar Hesti Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
