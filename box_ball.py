import cv2
import numpy as np

# อ่านภาพ
image = cv2.imread(r'C:\ProjectPYTHON\BotWithChicken\ball.png')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# กำหนดช่วงสี
lower_orange = np.array([5, 100, 100])
upper_orange = np.array([15, 255, 255])

# สร้าง Mask
mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

# ลดnoise
kernel = np.ones((5,5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# หาContours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # หาศูนย์กลาง
    M = cv2.moments(contour)
    if M["m00"] != 0:
        center_col = int(M["m10"] / M["m00"])
        center_row = int(M["m01"] / M["m00"])

        # หาขอบเขตของBoundingBox
        x, y, w, h = cv2.boundingRect(contour)

        # วาดBoundingBox
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # วาดจุดตรงกลาง
        cv2.circle(image, (center_col, center_row), 5, (0, 0, 255), -1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image, f'({center_col}, {center_row})', (x, y - 10), font, 0.5, (255, 255, 255), 2)

cv2.imshow('Ball with Bounding Box and Center', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
