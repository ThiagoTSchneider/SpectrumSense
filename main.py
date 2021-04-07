import cv2

cap = cv2.VideoCapture(1)

while True:
 ret, frames = cap.read()

 cv2.imshow("Video", frames)
 cv2.waitKey(0)