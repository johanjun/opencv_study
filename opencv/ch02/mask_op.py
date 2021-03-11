import cv2

src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:, :, -1]
src = src[:, :, 0:3]
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]

crop = dst[0:h, 0:w]

#src, dst는 타입이 같아야하고, mask는 무조건 grayscale
cv2.copyTo(src, mask, crop)
# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)

cv2.waitKey()
cv2.destroyAllWindows()