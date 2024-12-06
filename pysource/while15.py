prime=int(input('Melyik számot vizsgáljam? '))
kezd=1
db=0
while kezd <= prime:
    if prime%kezd==0:
        db+=1
    kezd+=1
if db==1:
    print('A szám relatív prím')
elif db==2:
    print('A szám prím')
else:
    print('A szám nem prím')