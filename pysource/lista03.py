import random
lst=[]
for i in range(100):
    lst.append(random.randint(10,100))
print(lst)
for i in range(100):
    if lst[i]>50:
        print(lst[i])