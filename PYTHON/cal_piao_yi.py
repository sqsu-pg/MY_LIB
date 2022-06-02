import argparse
from ctypes.wintypes import POINT

import numpy as np
import math

parse = argparse.ArgumentParser()
parse.add_argument('--txt_path', help='pose txt path')

args = parse.parse_args()

Pose_str = []

with open(args.txt_path, 'r') as f:
    for line in f.readlines():
        each_str = line.strip('\n')
        Pose_str.append(each_str)

First_pose_vec = Pose_str[0].split(' ')
Last_pose_vec = Pose_str[-1].split(' ')

First_x = float(First_pose_vec[3])
First_y = float(First_pose_vec[7])
First_z = float(First_pose_vec[11])

Last_x = float(Last_pose_vec[3])
Last_y = float(Last_pose_vec[7])
Last_z = float(Last_pose_vec[11])

delta_pose = math.sqrt((Last_x - First_x)* (Last_x - First_x) + (Last_y - First_y)* (Last_y - First_y) + (Last_z - First_z)* (Last_z - First_z) )

print ("漂移为: ", delta_pose)