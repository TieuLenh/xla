import cv2
import numpy as np
import matplotlib.pyplot as plt

# ĐỌC ẢNH
img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("Không đọc được ảnh")

# 1. HISTOGRAM
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(hist)
plt.show()

# 2. TĂNG / GIẢM ĐỘ SÁNG
brightness = 50
# tăng sáng
bright_img = cv2.convertScaleAbs(img, alpha=1, beta=brightness)
# giảm sáng
dark_img = cv2.convertScaleAbs(img, alpha=1, beta=-brightness)

# 3. OPEN / CLOSE
# kernel 5x5
kernel = np.ones((5, 5), np.uint8)
# OPEN = Erosion -> Dilation
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# CLOSE = Dilation -> Erosion
close_img = cv2.morphologyEx( img, cv2.MORPH_CLOSE, kernel)

# 4. SOBEL EDGE
# Sobel theo trục X
sobel_x = cv2.Sobel( img, cv2.CV_64F, 1, 0, ksize=3)
# Sobel theo trục Y
sobel_y = cv2.Sobel( img, cv2.CV_64F, 0, 1, ksize=3)
# Độ lớn gradient
sobel = cv2.magnitude(sobel_x, sobel_y)
sobel = np.uint8(np.absolute(sobel))

# 5. CANNY EDGE
canny = cv2.Canny( img, 100, 200)

# HIỂN THỊ
cv2.imshow("Original", img)

cv2.imshow("Bright", bright_img)
cv2.imshow("Dark", dark_img)

cv2.imshow("Open", open_img)
cv2.imshow("Close", close_img)

cv2.imshow("Sobel", sobel)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()