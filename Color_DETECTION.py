import cv2
import numpy as np

webcam = cv2.VideoCapture(1)

while True:
    ret, frame = webcam.read()

    cv2.imshow("Detecção de Cor Contínua", frame)

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_lower = np.array([148, 178, 111])
    red_upper = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, red_lower, red_upper)

    color_detected = cv2.bitwise_and(frame, frame, mask=red_mask)

    kernel = np.ones((5, 5), np.uint8)
    red_dilation = cv2.dilate(frame, kernel, 1)

    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            frame_with_rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Detectado", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            with open('dados_de_area.txt', 'a') as arquivo_area:
                arquivo_area.write(str(area) + '\n')

            cv2.imshow("Vídeo com Detecção de Cor", frame_with_rectangle)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
