import random
lst=[]
nagydb=0
for i in range(18):
    lst.append(random.randint(-20,20))

print(lst)

for i in range(len(lst)):
    if lst[i]>10:
        nagydb+=1
print('Tíztől nagyobb számból ennyit találtam:',nagydb)