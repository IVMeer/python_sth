# edge-detection.py
# Canny边缘检测
import cv2
import numpy as np
import matplotlib.pyplot as plt

import os 

print(os.getcwd())
# 读取图像
# image = cv2.imread('E:\\workspace\\python_demo\\Dec\\DL\\image.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(r'E:\workspace\python_demo\Dec\DL\stage-one\image.jpg', cv2.IMREAD_GRAYSCALE)


# 使用高斯滤波去噪
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Canny 边缘检测
edges = cv2.Canny(blurred_image, 100, 200)

# 显示原图与边缘图
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')

plt.show()


