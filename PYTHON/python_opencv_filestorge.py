import cv2
import numpy as np

fs = cv2.FileStorage('abc.yaml', cv2.FileStorage_WRITE)
mat1 = np.random.uniform(0, 1, [2, 2])
mat1 = np.linalg.inv(mat1)
mat1 = mat1.astype(np.float32)
fs.write('mat1', mat1)
fs.write('mat2', np.random.randint(0, 10, [2, 2]))
# arr.astype(np.float64) 
fs.write('num1', 1)
fs.write('num2', 2.5)
fs.write('str1', 'abc')
fs.write('str2', '你好')
# 关闭文件
fs.release()

fs2 = cv2.FileStorage('abc.yaml', cv2.FileStorage_READ)
mat1 = fs2.getNode('mat1').mat()
mat2 = fs2.getNode('mat2').mat()
num1 = fs2.getNode('num1').real()
num2 = fs2.getNode('num2').real()
str1 = fs2.getNode('str1').string()
str2 = fs2.getNode('str2').string()
# 关闭文件
fs2.release()

print(mat1)
print(mat2)
print(num1)
print(num2)
print(str1)
print(str2)
