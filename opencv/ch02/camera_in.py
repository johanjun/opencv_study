import sys
import cv2
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("camera open failed!")
    sys.exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # edge = cv2.Canny(frame, 100, 150)
    cv2.imshow('frame', frame)
    # cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27: #ESC
        break

cap.release()
cv2.destroyAllWindows()