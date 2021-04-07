import cv2
import numpy as np

web = cv2.VideoCapture(1)

while True:
    ocoiso, The_Thing = web.read()

    cv2.imshow("Web Continuously", The_Thing)

    hsv = cv2.cvtColor(The_Thing, cv2.COLOR_BGR2HSV)

    red_lower = np.array([136, 87, 111])
    red_higher = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv, red_lower, red_higher)

    COLOR_DETECTION = cv2.bitwise_and(The_Thing, The_Thing, mask=red_mask)

    Kernel = np.ones((5, 5), np.uint8)
    red_dilation = cv2.dilate(The_Thing, Kernel, 1)

    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            COLOR_DETECTION_IMAGE = cv2.rectangle(The_Thing, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(The_Thing, "Detected", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            with open('area_data.txt', 'a') as AreaData:
                AreaData.write(str(area) + '\n')

            cv2.imshow("COLOR_DETECTION_VIDEO", COLOR_DETECTION_IMAGE)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
