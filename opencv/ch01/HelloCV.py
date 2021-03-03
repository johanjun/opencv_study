import cv2
import sys

print("Hello, OpenCV", cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image load failed!")
    sys.exit()
#저장
cv2.imwrite('cat_gray.png', img)

#window 생성
cv2.namedWindow('image')

#window에 image를 보여주는 명령
cv2.imshow('image', img)

#esc(ascii 27)키보드 입력을 기다리며 image showing
#enter(13) / ord('key') / tab(9)
while True:
    if cv2.waitKey() == 27:
        break


#모든 window 닫기
cv2.destroyAllWindows()