import random
n=int(input())
list=[]
while True:
    if len(list)==n:
        break
    a=random.randint(1,20)
    if a not in list:
        list.append(a)
    
print(list)

