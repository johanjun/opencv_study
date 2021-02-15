import cv2
import sys

print("Hello, OpenCV", cv2.__version__)

img = cv2.imread('cat.bmp')

if img is None:
    print("Image load failed!")
    sys.exit()

#window 생성
cv2.namedWindow('image')

#window에 image를 보여주는 명령
cv2.imshow('image', img)

#키보드 입력을 기다리며 image showing
cv2.waitKey()

#모든 window 닫기
cv2.destroyAllWindows()