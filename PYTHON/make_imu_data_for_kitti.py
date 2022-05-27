'''
Author: your name
Date: 2022-02-07 16:00:25
LastEditTime: 2022-02-07 16:25:35
LastEditors: Please set LastEditors
FilePath: /PYTHON/make_imu_data_for_kitti.py
'''
import numpy as np 
import cv2 as cv 
import os
import argparse
import glob
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= "the path of imu data sets")

args = parser.parse_args()

print (args.path)

vec_imu_txt_data = glob.glob(os.path.join(args.path + '/*.txt'))
vec_imu_txt_data = sorted(vec_imu_txt_data)

all_acc_gyo_data = []

for imu_txt in vec_imu_txt_data:
    print (imu_txt)
    # all_data = np.loadtxt(imu_txt)
    # acc_gyo_data_np = np.zeros(6, dtype=np.float64)
    # acc_gyo_data_np[0:3] = all_data[11:14]
    # acc_gyo_data_np[3:6] = all_data[17:20]
    # all_acc_gyo_data.append(acc_gyo_data_np)

    with open(imu_txt, "r") as f:
        for line in f.readlines():
            str_imu_data = line.strip('\n')
            str_imu_data_vec = str_imu_data.split(' ')
            all_acc_gyo_data.append(str_imu_data_vec)

print ("所有的imu数据为: ", len(all_acc_gyo_data))

path_vec = args.path.split('/')

save_imu_data_txt = ''

for i in range(len(path_vec) - 1):
    if i > 0:
        save_imu_data_txt += '/'
        save_imu_data_txt += path_vec[i]

save_imu_data_txt += '/ImuData.txt'
print (save_imu_data_txt)

data_cols = [11, 12, 13, 17, 18, 19]

with open(save_imu_data_txt, 'w') as fw:
    for each_imu_data_str in all_acc_gyo_data:
        for index in data_cols:
            fw.write(each_imu_data_str[index])
            fw.write(' ')
        fw.write('\n')
    fw.close()