# 1. `cv2.imread()`
img = cv2.imread("test.jpg", cv2.IMREAD_GRAYSCALE)

| Parameter              | Ý nghĩa                     |
| ---------------------- | --------------------------- |
| `"test.jpg"`           | Đường dẫn ảnh               |
| `cv2.IMREAD_GRAYSCALE` | Đọc ảnh grayscale (ảnh xám) |

---
# 2. `cv2.calcHist()`
hist = cv2.calcHist([img], [0], None, [256], [0,256])

| Parameter | Ý nghĩa                    |
| --------- | -------------------------- |
| `[img]`   | Danh sách ảnh đầu vào      |
| `[0]`     | Channel cần tính histogram |
| `None`    | Mask (None = toàn ảnh)     |
| `[256]`   | Số bins histogram          |
| `[0,256]` | Khoảng giá trị pixel       |

---
# 3. `cv2.convertScaleAbs()`
bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
Công thức: g(x)=\alpha f(x)+\beta

| Parameter | Ý nghĩa               |
| --------- | --------------------- |
| `img`     | Ảnh đầu vào           |
| `alpha`   | Điều chỉnh contrast   |
| `beta`    | Điều chỉnh brightness |

Ví dụ:
| Giá trị     | Kết quả       |
| ----------- | ------------- |
| `alpha > 1` | Tăng contrast |
| `alpha < 1` | Giảm contrast |
| `beta > 0`  | Tăng sáng     |
| `beta < 0`  | Giảm sáng     |

---
# 4. `np.ones()`
kernel = np.ones((5,5), np.uint8)

| Parameter  | Ý nghĩa           |
| ---------- | ----------------- |
| `(5,5)`    | Kích thước kernel |
| `np.uint8` | Kiểu dữ liệu      |

---
# 5. `cv2.morphologyEx()`
open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

| Parameter        | Ý nghĩa         |
| ---------------- | --------------- |
| `img`            | Ảnh đầu vào     |
| `cv2.MORPH_OPEN` | Phép morphology |
| `kernel`         | Kernel xử lý    |

Các phép phổ biến:

| Operation         | Ý nghĩa            |
| ----------------- | ------------------ |
| `cv2.MORPH_OPEN`  | Erosion → Dilation |
| `cv2.MORPH_CLOSE` | Dilation → Erosion |

---
# 6. `cv2.Sobel()`
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

| Parameter    | Ý nghĩa             |
| ------------ | ------------------- |
| `img`        | Ảnh đầu vào         |
| `cv2.CV_64F` | Kiểu dữ liệu output |
| `1`          | Đạo hàm theo trục X |
| `0`          | Đạo hàm theo trục Y |
| `ksize=3`    | Kích thước kernel   |

Ví dụ:

| dx  | dy  | Ý nghĩa         |
| --- | --- | --------------- |
| `1` | `0` | Tách biên dọc   |
| `0` | `1` | Tách biên ngang |

---
# 7. `cv2.magnitude()`
sobel = cv2.magnitude(sobel_x, sobel_y)
Công thức: G=\sqrt{G_x^2+G_y^2}

| Parameter | Ý nghĩa         |
| --------- | --------------- |
| `sobel_x` | Gradient theo X |
| `sobel_y` | Gradient theo Y |

---
# 8. `np.absolute()`
np.absolute(sobel)

| Parameter | Ý nghĩa         |
| --------- | --------------- |
| `sobel`   | Ma trận đầu vào |

Mục đích: Chuyển giá trị âm thành dương - lấy trị tuyệt đối.

---
# 9. `cv2.Canny()`
canny = cv2.Canny(img, 100, 200)

| Parameter | Ý nghĩa     |
| --------- | ----------- |
| `img`     | Ảnh đầu vào |
| `100`     | Ngưỡng thấp |
| `200`     | Ngưỡng cao  |

Quy tắc:

| Gradient  | Kết quả           |
| --------- | ----------------- |
| `> upper` | Biên mạnh         |
| `< lower` | Loại bỏ           |
| Ở giữa    | Kiểm tra liên kết |

---
# 10. `cv2.imshow()`
cv2.imshow("Original", img)

| Parameter    | Ý nghĩa      |
| ------------ | ------------ |
| `"Original"` | Tên cửa sổ   |
| `img`        | Ảnh hiển thị |

---
# 11. `cv2.waitKey()`
cv2.waitKey(0)

| Parameter | Ý nghĩa     |
| --------- | ----------- |
| `0`       | Chờ vô hạn  |
| `1000`    | Chờ 1000 ms |

---
# 12. `cv2.destroyAllWindows()`
cv2.destroyAllWindows()
Mục đích: Đóng tất cả cửa sổ OpenCV.

---
# 13. `cv2.filter2D()`
conv = cv2.filter2D(img, -1, kernel)

| Parameter | Ý nghĩa            |
| --------- | ------------------ |
| `img`     | Ảnh đầu vào        |
| `-1`      | Giữ nguyên depth   |
| `kernel`  | Kernel convolution |

Mục đích: Áp dụng convolution custom.

---
# 14. `cv2.medianBlur()`
median = cv2.medianBlur(img, 3)

| Parameter | Ý nghĩa           |
| --------- | ----------------- |
| `img`     | Ảnh đầu vào       |
| `3`       | Kích thước kernel |

Mục đích: Khử nhiễu muối tiêu.

---
# 15. `cv2.blur()`
mean = cv2.blur(img, (3,3))

| Parameter | Ý nghĩa           |
| --------- | ----------------- |
| `img`     | Ảnh đầu vào       |
| `(3,3)`   | Kích thước kernel |

Mục đích: Mean filter (làm mịn trung bình).

---
# 16. `cv2.cvtColor()`
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

| Parameter           | Ý nghĩa          |
| ------------------- | ---------------- |
| `image`             | Ảnh đầu vào      |
| `cv2.COLOR_BGR2RGB` | Chuyển BGR → RGB |

---
# 17. `reshape()`
pixel_values = image_rgb.reshape((-1, 3))

| Parameter | Ý nghĩa         |
| --------- | --------------- |
| `-1`      | Tự tính số hàng |
| `3`       | 3 channel màu   |

Mục đích: Chuyển ảnh thành vector pixel.

---
# 18. `np.float32()`
pixel_values = np.float32(pixel_values)

Mục đích: Chuyển kiểu dữ liệu sang float32.

---
# 19. `cv2.kmeans()`

_, labels, centers = cv2.kmeans(
    pixel_values,
    k,
    None,
    criteria,
    10,
    cv2.KMEANS_RANDOM_CENTERS
)

| Parameter                   | Ý nghĩa                 |
| --------------------------- | ----------------------- |
| `pixel_values`              | Dữ liệu đầu vào         |
| `k`                         | Số cụm                  |
| `None`                      | Nhãn ban đầu            |
| `criteria`                  | Điều kiện dừng          |
| `10`                        | Số lần chạy             |
| `cv2.KMEANS_RANDOM_CENTERS` | Khởi tạo tâm ngẫu nhiên |

---
# 20. KMeans Criteria

criteria = (
    cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
    100,
    0.2
)

| Parameter                | Ý nghĩa                   |
| ------------------------ | ------------------------- |
| `TERM_CRITERIA_EPS`      | Dừng khi đạt độ chính xác |
| `TERM_CRITERIA_MAX_ITER` | Dừng khi đủ số vòng lặp   |
| `100`                    | Số vòng lặp tối đa        |
| `0.2`                    | Sai số tối thiểu          |

---
# 21. `flatten()`
labels = labels.flatten()
Mục đích: Chuyển mảng nhiều chiều thành 1 chiều.

---
# 22. `plt.subplot()`
plt.subplot(1,2,1)

| Parameter | Ý nghĩa              |
| --------- | -------------------- |
| `1`       | Số hàng              |
| `2`       | Số cột               |
| `1`       | Vị trí plot hiện tại |

---
# 23. `plt.imshow()`
plt.imshow(image_rgb)
Mục đích: Hiển thị ảnh bằng matplotlib.

---
# 24. `plt.axis('off')`
plt.axis('off')
Mục đích: Ẩn trục tọa độ.

---
# 25. `plt.tight_layout()`
plt.tight_layout()
Mục đích: Tự căn khoảng cách giữa các plot.
