import time

with open('withtest.txt','w') as f:
    f.write(time.strftime('%Y%m%d %H:%M:%S',time.localtime()))
   
with open('withtest.txt','r') as f:
    print(f.readlines())