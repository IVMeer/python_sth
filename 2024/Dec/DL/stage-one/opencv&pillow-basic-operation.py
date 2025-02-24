import cv2 
from PIL import Image, ImageFilter
image = Image.open(r'E:\workspace\python_demo\Dec\DL\image.jpg')
# pillow和opencv的图片格式不一样,PILLOW是RGB格式,opencv是BGR格式

# pillow库的一些基本操作
# 图片显示
# image.show()
# 调整图片大小
# resize_image = image.resize((300,300))
# resize_image.show()
# 图片裁剪
# cropped_image = image.crop((50,50,200,200))
# cropped_image.show()
# 图片旋转
# rotate_image  = image.rotate(45)
# rotate_image.show()
# 转为灰度图
# gray_image = image.convert('L')
# gray_image.show()
# 边缘检测
# edge_image = image.filter(ImageFilter.FIND_EDGES)
# edge_image.show()
# image.show()

# 接下来是opencv的一些图像基本操作
image = cv2.imread(r'E:\workspace\python_demo\Dec\DL\image.jpg')
# 图片显示
# cv2.imshow('Image',image)
# # 缩放
# resize_image = cv2.resize(image,(300,300))
# cv2.imshow('Resize Image')
# 裁剪
# cropped_image = image[50:200, 50:200]
# cv2.imshow("Cropped Image", cropped_image)
# 图像旋转
# 获取图像中心
# center = (image.shape[1] // 2, image.shape[0] // 2)
# 获取旋转矩阵
# rotation_martix = cv2.getRotationMatrix2D(center, 45, 1)
# 旋转图片
# rotation_image = cv2.warpAffine(image, rotation_martix, (image.shape[1],image.shape[0]))
# 显示旋转图片
# cv2.imshow('Rotation Image',rotation_image)
# gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# cv2.imshow('Gray Image', gray_image)
# 转换为灰度图
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny 边缘检测
edges = cv2.Canny(gray_image, 100, 200)

# 显示边缘检测结果
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()