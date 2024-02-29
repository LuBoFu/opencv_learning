import numpy as np
import matplotlib.pyplot as plt
import cv2


# 导入图片
img = cv2.imread('img/jpg1.jpg',flags=cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
# 写入灰度图片
cv2.imwrite('img/jpg1_gray.png',img)
# 按任意键，关闭弹框
cv2.waitKey(0)#若无wait则一闪而过

# arr = np.array([1,-2, 4, 16])
# func = np.poly1d(arr)
# # m=1表示求一阶导数，依次类推
# func1 = func.deriv(m=1)
# func2 = func.deriv(m=2)
# x = np.linspace(-4, 6, 100)#-4<=x<=6,分100个点

# y = func(x)
# y1 = func1(x)
# y2 = func2(x)

# print(func,'\n',func1,'\n',func2)
# print("多项式的根:")
# print(np.roots(func))

# plt.plot(x, y, label="{}".format(func))
# plt.plot(x, y1, label="{}".format(func1))
# plt.plot(x, y2, label="{}".format(func2))
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()

# plt.show()



# A=np.mat([[0, 1, 2],
#           [1, 1, 4],
#           [2, -1, 0]])
# print("矩阵A：")
# print(A)

# print("A的逆矩阵：")
# print(A.I)


# A = np.mat([[3, 2, 0, 5, 0],
#             [3, -2, 3, 6, -1],
#             [2, 0, 1, 5, -3],
#             [1, 6, -4, -1, 4]])

# print("矩阵A：")
# print(A)
# print("A的秩为：{}".format(np.linalg.matrix_rank(A)))

# print("A的转置矩阵：")
# print(A.T)


# array=[[1,2,3],[1,2,3],[4,6,2]]
# print("矩阵的秩:",np.linalg.matrix_rank(array))
