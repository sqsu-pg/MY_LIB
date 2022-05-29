import argparse
import numpy as np
import glob
import os
import cv2

from raw_data_func import ProcessTime

from raw_data_func import StrVecToSE3

from raw_data_func import TimeStrListToDelatTime

parse = argparse.ArgumentParser()

parse.add_argument('--calib_dir_path', help='path of raw data calib')
parse.add_argument('--imu_dir_path', help='path of raw data imu data')
parse.add_argument('--sync_image00_path', help='path of image_00 sync data')



args = parse.parse_args()

print("计算左目相机到imu的外参...")

calib_velo_to_cam_path = args.calib_dir_path + "/calib_velo_to_cam.txt"
calib_imu_to_velo_path = args.calib_dir_path + "/calib_imu_to_velo.txt"

print (calib_velo_to_cam_path)
print (calib_imu_to_velo_path)

T_cl = StrVecToSE3(calib_velo_to_cam_path)
print ('T_cl: ', T_cl)
T_lb = StrVecToSE3(calib_imu_to_velo_path)
print ('T_lb : ', T_lb)


T_c_b = np.matmul(T_cl, T_lb)
print ("T_cb 为: ")
print (T_c_b)

calib_imu_to_cam_path = args.calib_dir_path + '/calib_imu_to_cam.txt'

np.savetxt(calib_imu_to_cam_path, T_c_b, fmt='%s', delimiter=' ')

print ("T_c_b求逆矩阵,并保存为yaml格式")
calib_cam_to_body_yaml_path = args.calib_dir_path + '/calib_cam_to_imu.yaml'
print (calib_cam_to_body_yaml_path)
T_bc = np.linalg.inv(T_c_b)
T_bc = T_bc.astype(np.float32)

fs = cv2.FileStorage(calib_cam_to_body_yaml_path, cv2.FileStorage_WRITE)
fs.write('Tbc', T_bc)
fs.release()

print ("calib_Imu_to_cam 计算完成...")

print ("处理imu时间辍")

image_00_time_path = args.sync_image00_path + '/timestamps.txt'

imu_data_time_path = args.imu_dir_path + '/timestamps.txt'

image_sync_time_vec = []

with open(image_00_time_path, 'r') as f:
    for line in f.readlines():
        str_time = line.strip('\n')
        # print(str_time)  
        image_sync_time_vec.append(str_time)

imu_data_time_vec = []
with open(imu_data_time_path, 'r') as f:
    for line in f.readlines():
        str_time = line.strip('\n')
        # print(str_time)  
        imu_data_time_vec.append(str_time)

print ("比较imu第一个时间和图像第一个时间")
image_00_first_time = ProcessTime(image_sync_time_vec[0])
print ("图像第一个时间: ", image_00_first_time)
imu_first_time = ProcessTime(imu_data_time_vec[0])
print ("imu 第一个时间",imu_first_time)

flag_time = True
if image_00_first_time > imu_first_time:
    flag_time = False
else:
    flag_time = True

print ("处理image_00的时间辍")
img_str_time_list = []
imu_time_str_list = []

if flag_time==True:
    imu_time_str_list.append(image_sync_time_vec[0])
    imu_time_str_list.extend(imu_data_time_vec)
    img_str_time_list = image_sync_time_vec
else:
    imu_time_str_list = imu_data_time_vec
    img_str_time_list.append(imu_data_time_vec[0])
    img_str_time_list.extend(image_sync_time_vec)


delta_time_vec = TimeStrListToDelatTime(imu_time_str_list)

print ("检查imu时间辍是否有问题: ")
for i in range(len(delta_time_vec)):
    if delta_time_vec[i] <= 0:
        if flag_time == True:
            print ("IMU 第", i , '个时间辍有问题')
        else:
            print ("IMU 第", i+1 , '个时间辍有问题')

print ("保存 delta time")

img_delta_time_vec = TimeStrListToDelatTime(img_str_time_list)

save_delta_time_txt_path = args.imu_dir_path + '/delta_time.txt'
print (save_delta_time_txt_path)
with open(save_delta_time_txt_path, 'w') as fw:
    for time in delta_time_vec:
        tmp_e = '%e'%time
        fw.write(tmp_e)
        fw.write('\n')
    fw.close()

save_img_delta_time_txt_path = args.sync_image00_path + '/delta_time.txt'
print (save_img_delta_time_txt_path)
with open(save_img_delta_time_txt_path, 'w') as fw:
    for time in img_delta_time_vec:
        tmp_e = '%e'%time
        fw.write(tmp_e)
        fw.write('\n')
    fw.close()

save_imu_time_txt_path = args.imu_dir_path + '/imu_time.txt'
save_img_time_txt_path = args.sync_image00_path + '/img_time.txt'

imu_time_vec = []
sum_delta_time = 0.0

img_time_vec = []
img_sum_delta_time = 0.0

for i in range(len(delta_time_vec)):
    cur_time = sum_delta_time + delta_time_vec[i]
    sum_delta_time = cur_time
    imu_time_vec.append(cur_time)

for i in range(len(img_delta_time_vec)):
    cur_time = img_sum_delta_time + img_delta_time_vec[i]
    img_sum_delta_time = cur_time
    img_time_vec.append(cur_time)

print ("写imu_time.txt")
print ("写image0 txt")
print (save_img_time_txt_path)

if flag_time==True:
    #直接写
    with open(save_imu_time_txt_path, 'w') as fw:
        for imu_time in imu_time_vec:
            tmp_e = '%e'%imu_time
            fw.write(tmp_e)
            fw.write('\n')
        fw.close()
    
    #img需要先写0
    print ("img需要补充0")
    with open(save_img_time_txt_path, 'w') as fw:
        tmp_e = '%e'%0.0
        fw.write(tmp_e)
        fw.write('\n')
        fw.close()
    with open(save_img_time_txt_path, 'a') as fw:
        for img_time in img_time_vec:
            tmp_e = '%e'%img_time
            fw.write(tmp_e)
            fw.write('\n')
        fw.close()
    
else:
    #先写0
    print ("需要补充0")
    with open(save_imu_time_txt_path, 'w') as fw:
        tmp_e = '%e'%0.0
        fw.write(tmp_e)
        fw.write('\n')
        fw.close()
    with open(save_imu_time_txt_path, 'a') as fw:
        for imu_time in imu_time_vec:
            tmp_e = '%e'%imu_time
            fw.write(tmp_e)
            fw.write('\n')
        fw.close()
    
    #img 直接写
    with open(save_img_time_txt_path, 'w') as fw:
        for img_time in img_time_vec:
            tmp_e = '%e'%img_time
            fw.write(tmp_e)
            fw.write('\n')
        fw.close()
    
print ("保存imudata...")
imu_txt_data_dir_path = args.imu_dir_path + '/data'
vec_imu_txt_data = glob.glob(os.path.join(imu_txt_data_dir_path + '/*.txt'))


all_acc_gyo_data = []

for imu_txt in vec_imu_txt_data:
    # print (imu_txt)
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

save_imu_data_path = args.imu_dir_path + '/ImuData.txt'

data_cols = [11, 12, 13, 17, 18, 19]

with open(save_imu_data_path, 'w') as fw:
    for each_imu_data_str in all_acc_gyo_data:
        for index in data_cols:
            fw.write(each_imu_data_str[index])
            fw.write(' ')
        fw.write('\n')
    fw.close()