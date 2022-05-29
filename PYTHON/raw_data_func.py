import numpy as np


def ProcessTime(str_time):
    time_vec = str_time.split(' ')
    time = time_vec[-1]
    time_array = time.split('.')
    str_time_ms = time_array[-1]
    time_array = time_array[0].split(':')
    str_time_h = time_array[0]
    str_time_min = time_array[1]
    str_time_s =time_array[2]

    cur_time = 0
    cur_time += int(str_time_h)*3600
    cur_time += int(str_time_min)*60
    cur_time += int(str_time_s)

    tmp_ms = '0.' + str_time_ms
    tmp_ms = float(tmp_ms)
    cur_time += tmp_ms
    return cur_time


def StrVecToSE3(calib_path):
    calib_str_vec = []
    with open(calib_path, 'r') as f:
        for line in f.readlines():
            each_str = line.strip('\n')
            print (each_str)
            calib_str_vec.append(each_str)
    
    R_str_list = calib_str_vec[1].split(' ')
    t_str_list = calib_str_vec[2].split(' ')

    R_array = []
    t_array = []

    for i in range(1, len(R_str_list)):
        R_array.append(float(R_str_list[i]))
    for i in range(1, len(t_str_list)):
        t_array.append(float(t_str_list[i]))

    R_np = np.asarray(R_array)
    t_np = np.asarray(t_array)

    R_np = R_np.reshape(3, 3)
    t_np = t_np.reshape(3,)

    print (R_np.dtype)
    print (R_np)
    print (t_np.dtype)
    print (t_np)

    T_np = np.eye(4, 4, dtype=np.float64)

    T_np[0:3, 0:3] = R_np.copy()
    T_np[0:3, 3] = t_np.copy()
    print ("T_np 为: ")
    print (T_np)
    
    return T_np


def TimeStrListToDelatTime(time_str_list):
    time_all = []
    for str_time in time_str_list:
        time_all.append(ProcessTime(str_time))

    last_time = 0
    delta_time_vec = []

    for i in range(len(time_all)):
        if i == 0:
            last_time = time_all[i]

        else:
            cur_time = time_all[i]
            delta_time = cur_time - last_time
            last_time = cur_time
            delta_time_vec.append(delta_time)

    return delta_time_vec
            
