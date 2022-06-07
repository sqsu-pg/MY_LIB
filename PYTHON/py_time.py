# 例1：循环输出休眠1秒
import time
i = 1

start = time.time()
#long running
#do something other


while i <= 3:
    print (i) # 输出i
    i += 1
    time.sleep(1) # 休眠1秒

end = time.time()
print (end-start)