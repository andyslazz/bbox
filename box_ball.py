import cv2
import numpy as np

image = cv2.imread('ball.webp')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_orange = np.array([5, 100, 100])
upper_orange = np.array([15, 255, 255])

mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    center_row = y + h // 2
    center_col = x + w // 2
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.circle(image, (center_col, center_row), 5, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, f'Center_Row: {center_row}, Center_Col: {center_col}', (x,y-10), font, 0.5, (255, 255, 255), 2)

cv2.imshow('Balls with BB_BOX and Center', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
