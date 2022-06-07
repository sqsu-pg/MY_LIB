import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', help="timestamps.txt path")

args = parser.parse_args()

time_vec = []

with open(args.path, 'r') as f:
    for line in f.readlines():
        str_all = line.strip('\n')
        str_vec = str_all.split(',')
        time_str_vec = str_vec[1].split(':')
        time_str = time_str_vec[1]
        # print (time_str)
        time_vec.append(float(time_str))

sum_time = 0

for time in time_vec:
    sum_time = sum_time + time

mean_time = sum_time / len(time_vec)
print ("mean time : ", mean_time)