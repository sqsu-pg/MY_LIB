'''
Author: your name
Date: 2022-01-22 18:58:06
LastEditTime: 2022-01-22 19:33:14
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /PYTHON/mask_vis.py
'''
import numpy as np 
import cv2 as cv 
import os
import argparse
import glob
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--path', help= "the path of data sets")

args = parser.parse_args()

print (args.path)

mColor = {0:[255,0,0], 
            1:[0,255,0], 
            2:[0,0,255], 
            3:[255,255,0],
            4:[255,0,255], 
            5:[0,255,255], 
            6:[153,50,204], 
            7:[255,185,15],
            8:[0,139,69], 
            9:[175,238,238]} 



vec_mask_path = glob.glob(os.path.join(args.path + '/image_0_mask/', '*.txt'))
vec_mask_path = sorted(vec_mask_path)
vec_image_path = glob.glob(os.path.join(args.path + '/image_0/', '*.png'))
vec_image_path = sorted(vec_image_path)

# path = "/home/george/data_sets/03/image_0_mask/000000.txt"
if len(vec_image_path) != len(vec_mask_path):
    print ("error! the len of images and masks are not same!")
    sys.exit()

for image_path, mask_path in zip(vec_image_path, vec_mask_path):
    print (image_path)
    print (mask_path)
    image = cv.imread(image_path)
    Mask = np.loadtxt(mask_path)

    image_show = np.empty((image.shape[0], image.shape[1], 3), dtype= np.uint8)
    if len(image.shape) == 2:
        image_show[:, :, 0] = image.copy();
        image_show[:, :, 1] = image.copy();
        image_show[:, :, 2] = image.copy();
    else:
        image_show = image.copy();


    for i in range(Mask.shape[0]):
        for j in range(Mask.shape[1]):
            if Mask[i, j] != 0:
                image_show[i, j, 0] = mColor[Mask[i, j] % 10][0]
                image_show[i, j, 1] = mColor[Mask[i, j] % 10][1]
                image_show[i, j, 2] = mColor[Mask[i, j] % 10][2]
    
    image_both_show = np.concatenate([image, image_show], axis=0)
    cv.imshow("mask vis", image_both_show)
    cv.waitKey()











