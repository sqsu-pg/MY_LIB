from ast import arg
from hashlib import new
import numpy as np 
import cv2 as cv 
import os
import argparse
import glob
import sys
import math


parse = argparse.ArgumentParser()
parse.add_argument("--data_sets_path",help= "输入需要删除前多少个数据的数据及路径，包括光流和掩码")
parse.add_argument("--num", help="需要删除前多少帧")

args = parse.parse_args()

img_0_path = args.data_sets_path + "/image_0/"
img_1_path = args.data_sets_path + "/image_1/"
mask_path = args.data_sets_path + "/image_0_mask/"
flo_path = args.data_sets_path + "/flow/"

print (img_0_path)
print (img_1_path)
print (mask_path)
print (flo_path)

for i in range(int(args.num)):
    new_name = str(i)
    new_name = new_name.zfill(6)
    new_name = new_name + '.png'
    delete_name = img_0_path + new_name
    os.remove(delete_name)
    print ("remove png ： ", delete_name)

for i in range(int(args.num)):
    new_name = str(i)
    new_name = new_name.zfill(6)
    new_name = new_name + '.png'
    delete_name = img_1_path + new_name
    os.remove(delete_name)
    print ("remove png ： ", delete_name)

for i in range(int(args.num)):
    delete_name_mask = str(i)
    delete_name_mask =delete_name_mask.zfill(6)
    delete_name_mask = delete_name_mask + '.txt'
    delete_name_mask = mask_path + delete_name_mask
    os.remove(delete_name_mask)
    print("remove mask : ", delete_name_mask)

for i in range(int(args.num)):
    delete_name_flo = str(i)
    delete_name_flo =delete_name_flo.zfill(6)
    delete_name_flo = delete_name_flo + '.flo'
    delete_name_flo = flo_path + delete_name_flo
    os.remove(delete_name_flo)
    print("remove mask : ", delete_name_flo)



