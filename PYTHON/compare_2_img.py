import numpy as np 
import cv2 as cv 
import os
import argparse
import glob
import sys
import math

def sum_of_numpy(img):
    res = 0
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            res += abs(img[i][j])
    
    return res


parser = argparse.ArgumentParser()
parser.add_argument('--img1_path', help= "the path of data sets")
parser.add_argument('--img2_path', help= "the path of data sets")

args = parser.parse_args()

print (args.img1_path)
print (args.img2_path)

img1 = cv.imread(args.img1_path, cv.IMREAD_UNCHANGED)
print (img1.shape)
img2 = cv.imread(args.img2_path, cv.IMREAD_UNCHANGED)
print (img2.shape)

compare_img = img1 - img2

if sum_of_numpy(compare_img) != 0:
    print ("不相同")
else:
    print ("相同")