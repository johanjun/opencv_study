import sys
import glob #특정 패턴의 filename을 토대로 전부 호출
import cv2


# 이미지 파일을 모두 img_files 리스트에 추가
img_files = glob.glob('.//images//*.jpg')
for f in img_files:
    print(f)
# 전체 화면으로 'image' 창 생성
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 무한 루프
cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])
    cv2.imshow("image", img)
    if cv2.waitKey(1000) == 27:
        break

    idx += 1
    if idx >= cnt:
        idx = 0
cv2.destroyAllWindows()