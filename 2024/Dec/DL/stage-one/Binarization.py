# 灰度化 二值化 边缘检测【初识】
# 二值化Binarization
import cv2 
import matplotlib.pyplot as plt
# 确定图像位置
image = cv2.imread(r'E:\workspace\python_demo\Dec\DL\stage-one\image.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 灰度化 Grayscale
# 将图像转换为灰度图像
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 显示图像
# plt.imshow(gray_image, cmap='gray')
# plt.title("Grayscale Image")
# plt.show()

# 使用固定阈值进行二值化
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 显示图像
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image")
plt.show()

#
# 使用 Sobel 算子进行边缘检测
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)  # 水平方向
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)  # 垂直方向

# 计算总边缘强度（梯度幅值）
sobel_edge = cv2.magnitude(sobel_x, sobel_y)

# 显示边缘图
# plt.imshow(sobel_edge, cmap='gray')
# plt.title("Sobel Edge Detection")
# plt.show()

# 综合使用 灰度化、二值化、边缘检测
# 读取图片
image = cv2.imread(r'E:\workspace\python_demo\Dec\DL\stage-one\image2.jpg')
# 1. 灰度化处理
gray_image =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 2. 二值化处理
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# 3. Sobel 边缘检测
sobel_x = cv2.Sobel(binary_image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(binary_image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edge = cv2.magnitude(sobel_x, sobel_y)

# 4. 显示结果
plt.figure(figsize=(10, 5))

plt.subplot(1, 3, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')

plt.subplot(1, 3, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

plt.subplot(1, 3, 3)
plt.imshow(sobel_edge, cmap='gray')
plt.title('Sobel Edge Detection')

plt.tight_layout()
plt.show()



"""
KNN→SVM→决策树
"""