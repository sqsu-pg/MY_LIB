'''
Author: your name
Date: 2022-01-29 21:00:48
LastEditTime: 2022-05-21 21:07:48
LastEditors: sqsu-pg 18846049359@163.com
FilePath: /PYTHON/convert_kitti_timestamps.py
'''
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', help="timestamps.txt path")

args = parser.parse_args()

print (args.path)

time_list = []
##对齐imu数据和图像数据使用的
time_list.append('2011-09-30 12:40:25.042733312')

with open(args.path, "r") as f:
    for line in f.readlines():
        str_time = line.strip('\n')
        print(str_time)
        time_list.append(str_time)

time_all = []

for str_time in time_list:
    str_time = str_time.split(' ')
    str_time = str_time[-1]
    str_time = str_time.split('.')
    str_time_ms = str_time[-1]
    str_time = str_time[0].split(':')
    str_time_h = str_time[0]
    str_time_min = str_time[1]
    str_time_s = str_time[2]
    tmp_list = []
    tmp_list.append(str_time_h)
    tmp_list.append(str_time_min)
    tmp_list.append(str_time_s)
    tmp_list.append(str_time_ms)
    time_all.append(tmp_list)
    print (tmp_list)

##重新生成时间，单位为s

time_s_to_txt = []

last_time = 0

for i in range(len(time_all)):
    if i == 0:
        time_s_to_txt.append(0)
        
        last_time += int(time_all[i][0]) * 3600
        last_time += int(time_all[i][1]) * 60
        last_time += int(time_all[i][2])

        tmp_ms = '0.'+time_all[i][3]
        tmp_ms = float(tmp_ms)
        last_time = float(last_time)
        last_time += tmp_ms

    else:
        delta_time = 0
        cur_time = 0
        cur_time += int(time_all[i][0]) * 3600
        cur_time += int(time_all[i][1]) * 60
        cur_time += int(time_all[i][2])

        tmp_ms = '0.'+time_all[i][3]
        tmp_ms = float(tmp_ms)
        cur_time = float(cur_time)
        cur_time += tmp_ms

        delta_time = cur_time - last_time
        last_time = cur_time
        time_s_to_txt.append(delta_time)

##遍历time_s_to_txt保存起来
save_delta_time_txt = ''

path_vec = args.path.split('/')
for i in range(len(path_vec) - 1):
    if i > 0:
        save_delta_time_txt += '/'
        save_delta_time_txt += path_vec[i]

save_delta_time_txt += '/delta_time.txt'
print (save_delta_time_txt)


with open(save_delta_time_txt, 'w') as fw:
    for time in time_s_to_txt:
        tmp_e = '%e'%time
        fw.write(tmp_e)
        fw.write('\n')
    fw.close()
        

save_time_txt = ''
path_vec = args.path.split('/')
for i in range(len(path_vec) - 1):
    if i > 0:
        save_time_txt += '/'
        save_time_txt += path_vec[i]

save_time_txt += '/time.txt'
print (save_time_txt)

sum_delta_time = 0.0
with open(save_time_txt, 'w') as fw:
    for delta_time in time_s_to_txt:
        cur_time = sum_delta_time + delta_time
        sum_delta_time = cur_time
        tmp_e = '%e'%cur_time
        fw.write(tmp_e)
        fw.write('\n')
    fw.close()