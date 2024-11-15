bedb=1
szam= int(input('Kérek egy öttel osztható számot! '))
while szam%5!=0:
    szam = int(input('Kérek egy öttel osztható számot! '))
    bedb+=1
print(bedb,'. alkalommal írtál helyes számot!')
