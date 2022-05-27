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



vec_image_path = glob.glob(os.path.join(args.path + '/image_0/', '*.png'))
vec_image_path = sorted(vec_image_path)


for image_path in vec_image_path:
    print (image_path)
    image = cv.imread(image_path)

    cv.imshow("kitti vis", image)
    cv.waitKey(30)











