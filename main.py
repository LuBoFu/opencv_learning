import cv2

# 导入图片
img = cv2.imread('img/jpg1.jpg')
cv2.imshow('image', img)

# 按任意键，关闭弹框
cv2.waitKey(0)