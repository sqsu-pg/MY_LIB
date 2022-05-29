'''
Author: your name
Date: 2022-01-26 21:06:58
LastEditTime: 2022-01-26 21:22:50
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import numpy as numpy
import cv2 as cv
import os
import argparse
import glob
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= "the sets path needed to rename")

args = parser.parse_args()

print(args.path)

# vec_image_path = glob.glob(os.path.join(args.path, '/*.png'))
# vec_image_path = sorted(vec_image_path)

vec_image_path = os.listdir(args.path)
vec_image_path = sorted(vec_image_path)

print (vec_image_path)

for i in range(len(vec_image_path)):
    new_name = str(i)
    new_name = new_name.zfill(6)
    new_name = new_name + '.flo'
    print (new_name)
    new_name = args.path + '/' + new_name

    vec_image_path[i] = args.path + '/' + vec_image_path[i]
    os.rename(vec_image_path[i], new_name)
    print(vec_image_path[i])