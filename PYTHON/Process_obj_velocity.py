import argparse
from xml.sax.handler import DTDHandler
import numpy as np
import matplotlib.pyplot as plt
parser = argparse.ArgumentParser()
parser.add_argument('--path_txt', help="obj veolcity txt path")

args = parser.parse_args()

print (args.path_txt)

obj_id_and_vel_str_vec = []

with open(args.path_txt, 'r') as f:
    for line in f.readlines():
        each_str = line.strip('\n')
        print(each_str)
        obj_id_and_vel_str_vec.append(each_str)

id_vec = []
velocity_vec = []

id_dict = {}

for str in obj_id_and_vel_str_vec:
    str_vec = str.split(',')
    id_str = str_vec[0]
    vel_str = str_vec[1]
    id_vec = id_str.split(':')
    id = id_vec[1]
    print ("obj id :", id)
    print (len(id))


    vel_vec = vel_str.split(':')
    vel = vel_vec[1]
    print ("vel :", vel)
    print (len(vel))

    if id in id_dict:
        id_dict[id].append(vel)
    else:
        id_dict[id] = []
        id_dict[id].append(vel)


print ("sudu dict : ")
print (id_dict)

for keys in id_dict.keys():
    print ("id: ", keys, "len: ", len(id_dict[keys]))

x_4_vec = []
y_4_vec = []
for i in range(len(id_dict['4'])):
    x_4_vec.append(i)
    y_4_vec.append(float(id_dict['4'][i]))


x_6_vec = []
y_6_vec = []
for i in range(len(id_dict['6'])):
    x_6_vec.append(i)
    y_6_vec.append(float(id_dict['6'][i]))

x_4 = np.asarray(x_4_vec, dtype=int)
y_4 = np.asarray(y_4_vec, dtype=float)

x_6 = np.asarray(x_6_vec, dtype=int)
y_6 = np.asarray(y_6_vec, dtype=float)


plt.title('Obj Vel') #写上图题
plt.xlabel('x') #为x轴命名为“x”
plt.ylabel('Vel') #为y轴命名为“y”
# plt.xlim(0,1) #设置x轴的范围为[0,1]
# plt.ylim(0,1) #同上
# plt.xticks([0,0.2,0.4,0.6,0.8,1]) #设置x轴刻度
# plt.yticks([0,0.2,0.4,0.6,0.8,1]) #设置y轴刻度
# plt.tick_params(labelsize = 20) #设置刻度字号
plt.plot(x_4,y_4) #第一个data表示选取data为数据集，第二个是函数，data的平方
plt.plot(x_6,y_6) #同上
plt.legend(['Obj3','Obj5']) #打出图例
plt.show() #显示图形
