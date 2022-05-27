'''
Author: your name
Date: 2022-02-07 13:28:14
LastEditTime: 2022-02-07 15:01:36
LastEditors: Please set LastEditors
FilePath: /PYTHON/cal_kitti_b_c.py
'''
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path_1', help="calib_velo_to_cam.txt path")
parser.add_argument('--path_2', help="calib_imu_to_velo.txt path")

args = parser.parse_args()

print (args.path_1)
print (args.path_2)


calib_velo_to_cam_str = []
calib_imu_to_velo_str = []

with open(args.path_1, 'r') as f:
    for line in f.readlines():
        each_str = line.strip('\n')
        print (each_str)
        calib_velo_to_cam_str.append(each_str)

with open(args.path_2, 'r') as f:
    for line in f.readlines():
        each_str = line.strip('\n')
        print (each_str)
        calib_imu_to_velo_str.append(each_str)

R_cl_str_list = calib_velo_to_cam_str[1].split(' ')
T_cl_str_list = calib_velo_to_cam_str[2].split(' ')

R_cl_array = []
T_cl_array = []

for i in range(1, len(R_cl_str_list)):
    R_cl_array.append(float(R_cl_str_list[i]))

for i in range(1, len(T_cl_str_list)):
    T_cl_array.append(float(T_cl_str_list[i]))


R_cl = np.asarray(R_cl_array)
R_cl = R_cl.reshape(3, 3)
print (R_cl.dtype)
print (R_cl)

T_cl = np.asarray(T_cl_array)
T_cl = T_cl.reshape(3,)
print (T_cl.dtype)
print (T_cl)


R_lb_str_list = calib_imu_to_velo_str[1].split(' ')
T_lb_str_list = calib_imu_to_velo_str[2].split(' ')

R_lb_array = []
T_lb_array = []

for i in range(1, len(R_lb_str_list)):
    R_lb_array.append(float(R_lb_str_list[i]))

for i in range(1, len(T_lb_str_list)):
    T_lb_array.append(float(T_lb_str_list[i]))


R_lb = np.asarray(R_lb_array)
R_lb = R_lb.reshape(3, 3)
print (R_lb.dtype)
print (R_lb)

T_lb = np.asarray(T_lb_array)
T_lb = T_lb.reshape(3,)
print (T_lb.dtype)
print (T_lb)

T_c_l = np.eye(4, 4, dtype=np.float64)
T_l_b = np.eye(4, 4, dtype=np.float64)

T_c_l[0:3, 0:3] = R_cl.copy()
T_c_l[0:3, 3] = T_cl.copy()
print ("T_c_l 为: ")
print (T_c_l)

T_l_b[0:3, 0:3] = R_lb.copy()
T_l_b[0:3, 3] = T_lb.copy()
print ('T_l_b 为: ')
print (T_l_b)

T_c_b = np.matmul(T_c_l, T_l_b)
print ("T_cb 为: ")
print (T_c_b)

np.savetxt('./calib_imu_to_cam.txt', T_c_b, fmt='%s', delimiter=' ')
