import numpy as np
import sys
import cv2

# img1 = np.empty((240, 320), dtype=np.uint8)
# img2 = np.zeros((240, 320, 3), dtype=np.uint8)
# img3 = np.ones((240, 320, 3), dtype=np.uint8) * 255
# img4 = np.full((240, 320), fill_value=128, dtype=np.uint8)


# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.imshow('img4', img4)

img1 = cv2.imread('HappyFish.jpg')
img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

# img1[:, :] = (0, 255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()

cv2.destroyAllWindows()