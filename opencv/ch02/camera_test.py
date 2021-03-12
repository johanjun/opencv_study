import cv2

cam = cv2.VideoCapture(1)
print(cam.isOpened())
cam.release()