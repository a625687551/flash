import time
a = time.time() + 3600
a1 = time.localtime(a)
a2 = time.strftime("%Y-%m-%d %H:%M:%S", a1)

print(a2)
print("laitaihua自动创建于:" + (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))
print(str(time.strftime("%Y-%m-%d %H:%M:00", time.localtime(time.time() + 7200))))