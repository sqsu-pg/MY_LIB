'''
Author: your name
Date: 2022-01-29 21:58:59
LastEditTime: 2022-05-21 21:03:05
LastEditors: sqsu-pg 18846049359@163.com
FilePath: /PYTHON/vis_kitti_timestamps.py
'''
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--path', help="timestamps.txt path")

args = parser.parse_args()

print (args.path)

time_list = []

with open(args.path, "r") as f:
    for line in f.readlines():
        str_time = line.strip('\n')
        print(str_time)
        time_list.append(str_time)

# time_all = []

# for str_time in time_list:
#     str_time = str_time.split(' ')
#     str_time = str_time[-1]
#     str_time = str_time.split('.')
#     str_time_ms = str_time[-1]
#     str_time = str_time[0].split(':')
#     str_time_h = str_time[0]
#     str_time_min = str_time[1]
#     str_time_s = str_time[2]
#     tmp_list = []
#     tmp_list.append(str_time_h)
#     tmp_list.append(str_time_min)
#     tmp_list.append(str_time_s)
#     tmp_list.append(str_time_ms)
#     time_all.append(tmp_list)
#     print (tmp_list)

time_s = []

# for time_iter in time_all:
#     tmp_time = 0
#     # tmp_time += float(time_iter[0] * 3600)
#     tmp_time += float(time_iter[1]) * 60
#     tmp_time += float(time_iter[2])

#     a = '0.'
#     a += time_iter[3]
#     tmp_time += float(a)
    
#     time_s.append(tmp_time)

for i in range (0, len(time_list)):
    time_s.append(float(time_list[i]))

for i in range(1, len(time_s)):
    if time_s[i] < time_s[i-1]:
        print ("false : ", i)

x_label = np.arange(0, len(time_s))
print (x_label.shape)

y_label = np.asarray(time_s, dtype= float)

print (y_label)

plt.scatter(x_label, y_label, marker ='o', )
plt.show()