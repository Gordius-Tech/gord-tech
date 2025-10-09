listam = [3, 7, -2, 15, 0, -8, 21, 14, -5, 6]

print('1. feladat')
print(listam)
"""
for i in range(len(listam)):
    print(listam[i])
"""

print('2. feladat')
print('A lista összesen ennyi elemből áll:',len(listam))

print('3. feladat')
for i in range(len(listam)):
    if (i+1) % 3 == 0:
        print(i+1,'. elem a:',listam[i])

"""
for i in range(2,len(listam),3):
    print(i+1,'. elem b:',listam[i])
"""

print('4. feladat')
for i in range(len(listam)-1,-1, -1):
    print(listam[i])
"""
for i in range(9,-1,-1):
    print(listam[i])
"""

print('5. feladat')
szum=0
for i in range(len(listam)):
    szum+=listam[i]
print('A lista elemeinek az összege:',szum)

print('6. feladat')
max=min=listam[0]
for i in range(len(listam)):
    if listam[i]>max:
        max=listam[i]
    if listam[i]<min:
        min=listam[i]
print('Legkisebb elem:',min,'legnagyobb elem',max)

print('7. feladat')
szum=0
for i in range(len(listam)):
    if listam[i]>0:
        szum+=listam[i]
print('A pozitív számok összege:',szum)

print('8. feladat')
neglist=[]
for i in range(len(listam)):
    if listam[i]<0:
        neglist.append(listam[i])
print('A negatív számok lista tartalma:',neglist)

print('9. feladat')
pozdb=0
for i in range(len(listam)):
    if listam[i]>0:
        pozdb+=1
print('Ennyi pozitív szám van a listában:',pozdb)

print('10. feladat')
ujlista=[]
for i in range(len(listam)):
    ujlista.append(listam[i]*2)
print('Az eredeti lista elemeinek a duplája:',ujlista)

print('11. feladat')
abszlist=[]
for i in range(len(listam)):
    if listam[i]<0:
        abszlist.append(listam[i]*(-1))
    else:
        abszlist.append(listam[i])
print('A lista elemeinek abszolút értéke: ',abszlist)

print('12. feladat')
keres=int(input('Melyik számot keressük a listában?'))
van=False
for i in range(len(listam)):
    if listam[i]==keres:
        van=True
        print('Benne van a listában')
        break
if van==False:
    print('Nincs benne a listában')

print('13. feladat')
szam=int(input('Melyik számtól keressünk nagyobbat?'))
db=0
for i in range(len(listam)):
    if listam[i]>szam:
        db+=1
print('A(z)',szam,'számtól nagyobb értékek száma: ',db)

print('14. feladat')
szam=int(input('Melyik számtól keressünk kisebbet?'))
for i in range(len(listam)):
    if listam[i]<szam:
        print(szam,'számtól kisebb a(z)',i+1,'. helyen lévő',listam[i])

print('15. feladat')
par=partlan=0
for i in range(len(listam)):
    if listam[i]%2==0:
        par=par+listam[i]*2
    else:
        par=par+listam[i] * 2

print('Páros számokból létrehozott érték:',par,'páratlan számokból létrehozott érték:',partlan)

print('16. feladat')
for i in range(len(listam)):
    if listam[i]>10:
        listam[i]=0
print('Végső lista elemei:',listam)