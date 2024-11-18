#1. megoldas
eredmeny=1
fakt = int(input('Hányas szám faktoriálisát számoljam ki? '))
kezd=1
while fakt>=kezd:
    eredmeny*=kezd
    kezd+=1
print(fakt,' faktoriálisa: ',eredmeny)

#2. megoldas
eredmeny=1
fakt = int(input('Hányas szám faktoriálisát számoljam ki? '))
while fakt >0:
    eredmeny*=fakt
    fakt-=1
print('Az eredmény: ',eredmeny)