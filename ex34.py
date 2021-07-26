num = int(input())

sal = num*0.15 + num
sal1 = num*0.10 + num

if num < 1250:  
    print(sal)
else:
    print(sal1)