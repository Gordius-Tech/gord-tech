import random
lista=[]
for i in range(20):
    lista.append(random.randint(0,100))
print(lista)

for i in range(20):
    if i % 2 != 0:
        print(lista[i])

"""
print(lista[1::2])

for i in range(1,len(lista),2):
    print(lista[i])
"""