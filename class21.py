import time

Time = time.localtime()

nowtime =time.strftime('%H:%M:%S', Time)
print(nowtime)