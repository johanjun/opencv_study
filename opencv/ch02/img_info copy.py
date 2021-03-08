import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print("Image load failed!")
# 영상의 속성 참조
print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)


# 영상의 크기 참조
h, w = img1.shape[:2]
print('w X h = {} X {}'.format(w, h))

# h, w, d = img2.shape
# print('w X h X d = {} X {} X {}'.format(w, h, d))

h, w = img2.shape[:2]
print('w X h = {} X {}'.format(w, h))


if len(img1.shape) == 2:
    print('img1 is a grayscale image')

# 영상의 픽셀 값 참조
# x = 20
# y = 10
# p1 = img1[y, x]
# print(p1)

# p2 = img2[y, x]
# print(p2) #BGR

#아래와 같은 코드는 병목 발생시킬수있음
# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 0 #black
#         img2[y, x] = (0, 255, 255) #yellow

# 아래처럼
img1[:,:] = 0
img2[:,:] = (0, 255, 255)

#show
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()