import cv2 as cv
# for i in range():
#     pass
# for i in range(10):
#     src = cv.imread('E:\\workspace\\python_demo\\digits\\'+str(i)+'.jpg')#读取图片
#     gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
#     ret, binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)#白底黑字转换为黑底白字
#     cv.imwrite('E:\\workspace\\python_demo\\digits_processed\\new'+str(i)+'.jpg', binary)#将图像数据写入到图像文件中


src = cv.imread('E:\\workspace\\python_demo\\digits\\0.jpg')#读取图片
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret, binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)#白底黑字转换为黑底白字
# cv.imwrite('E:\\workspace\\python_demo\\digits_processed\\new0.jpg', binary)#将图像数据写入到图像文件中

cv.imwrite('new0.jpg', binary)