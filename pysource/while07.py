#1. megoldás
szum=szam=0
while szam<=100:
    if  szam%3==0:
        szum+=szam
    szam+=1
print('1-100-ig a hárommal osztható számok összege: ',szum)

#2. megoldás (egyszerű de nagyszerű)
szum=0
szam=3
while szam<=100:
    szum+=szam
    szam+=3
print('1-100-ig a hárommal osztható számok összege: ',szum)