import cv2 as cv2
import numpy as np

img = cv2.imread("img/aan.tiff")
cv2.imshow("Gambar Original", img)
kernel = np.ones((5,5), np.uint8)
erosian = cv2.erode(img, kernel, iterations = 1)
cv2.imshow("Erosion", erosian)

dilation = cv2.dilate(img, kernel, iterations = 1)
cv2.imshow("Dilasi", dilation)

kernell = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernell)
cv2.imshow('Opening', opening)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)

cv2.waitKey(0)
cv2.destroyWindow()