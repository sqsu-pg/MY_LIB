import argparse
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument('--kitti_data_set_path', help="kitti_data_path")
parser.add_argument('--delete_rate', help='rate of delete ...')
parser.add_argument('--is_remove_png', help='remove enter')

args = parser.parse_args()

print (args.kitti_data_set_path)

kitti_image_0_path = args.kitti_data_set_path + "/image_0"

kitti_image_1_path = args.kitti_data_set_path + "/image_1"
kitti_gray_time_path = args.kitti_data_set_path + "/times.txt"


# kitti_color_path = args.kitti_data_set_path + "/image_0"


vec_image0_path = glob.glob(os.path.join(kitti_image_0_path + '/', '*.png'))
vec_image0_path = sorted(vec_image0_path)
# print (len(vec_image0_path))

# for image0_path in vec_image0_path:
#     print(image0_path)

vec_image1_path = glob.glob(os.path.join(kitti_image_1_path + '/', '*.png'))
vec_image1_path = sorted(vec_image1_path)

image_gray_time_vec = []

with open(kitti_gray_time_path, 'r') as f:
    for line in f.readlines():
        str_time = line.strip('\n')
        # print(str_time)  
        image_gray_time_vec.append(str_time)

print (len(image_gray_time_vec))

if len(vec_image1_path) != len(vec_image0_path) or len(vec_image0_path) != len(image_gray_time_vec):
    print ("kitti data set has size problem")

delete_rate = int(args.delete_rate)

image_0_delete_vec = []
image_1_delete_vec = []
image_gray_time_delete_vec = []

for i in range(len(vec_image0_path)):
    if i % delete_rate != 0:
        image_0_delete_vec.append(vec_image0_path[i])
        image_1_delete_vec.append(vec_image1_path[i])
        image_gray_time_delete_vec.append(image_gray_time_vec[i])
        # print (vec_image0_path[i])

remove_flag = bool(args.is_remove_png)

new_gray_time_vec = []

if remove_flag == True:
    #删除图像
    for i in range(len(image_0_delete_vec)):
        os.remove(image_0_delete_vec[i])
        os.remove(image_1_delete_vec[i])
    for j in range(len(image_gray_time_vec)):
        if j % delete_rate == 0:
            new_gray_time_vec.append(image_gray_time_vec[j])
    print ("重写时间函数")
    print ("new times len is : ", len(new_gray_time_vec))

    # with open(kitti_gray_time_path, 'w') as fw:
    #     fw.close()
    with open(kitti_gray_time_path, 'w') as fw:
        for time in new_gray_time_vec:
            # time = float(time)
            # tmp_e = '%e'%time
            tmp_e = time
            fw.write(tmp_e)
            fw.write('\n')
        fw.close()

else:
    #没有删除图像
    print ("没有删除图像和时间辍")

#重新给图片编号

new_vec_image0_path = glob.glob(os.path.join(kitti_image_0_path + '/', '*.png'))
new_vec_image0_path = sorted(new_vec_image0_path)
print (len(new_vec_image0_path))


new_vec_image1_path = glob.glob(os.path.join(kitti_image_1_path + '/', '*.png'))
new_vec_image1_path = sorted(new_vec_image1_path)

for i in range(len(new_vec_image0_path)):
    new_name = str(i)
    new_name = new_name.zfill(6)
    new_name = new_name + '.png'
    print (new_name)
    new_name = kitti_image_0_path + '/' + new_name

    os.rename(new_vec_image0_path[i], new_name)
    # print (new_vec_image0_path[i])

for i in range(len(new_vec_image1_path)):
    new_name = str(i)
    new_name = new_name.zfill(6)
    new_name = new_name + '.png'
    print (new_name)
    new_name = kitti_image_1_path + '/' + new_name

    os.rename(new_vec_image1_path[i], new_name)
    # print (new_vec_image1_path[i])