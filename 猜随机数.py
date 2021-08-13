import random
import time
i=1
s1=random.randint(0,100)
cs1=int(input('请输入1~100中的一个数字:'))
while s1!=cs1:
    if s1>cs1:
        print('你第'+str(i)+'次输入的数字小于随机数字')
        cs1=int(input('请再次输入数字:'))
    else:
        print('你第'+str(i)+'次输入的数字大于随机数字')
        cs1=int(input('请再次输入数字:'))
    i+=1
print('恭喜你,你第'+str(i)+'次输入的数字与随机数字一样!')
time.sleep(30)
