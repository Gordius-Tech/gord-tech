bevetelek = [
    25000, 21000, 18000, 27000, 22000, 23000, 21000, 19000, 24000, 21000,
    20000, 25000, 26000, 19000, 22000, 24000, 26000, 23000, 21000, 25000,
    28000, 30000, 29000, 25000, 22000, 27000, 26000, 24000, 23000, 25000
]

#1. feladat
napokdb=len(bevetelek)
print('1. feladat: A vizsgált hónap',napokdb, 'napos volt.')

#2. feladat
max=bevetelek[0]
index=0
for i in range(napokdb):
    if bevetelek[i]>max:
        max=bevetelek[i]
        index=i
print('2. feladat: A legnagyobb bevétel a listában itt található:',index,'és ennyi volt:',max,'Ft.')

#3. feladat
min=bevetelek[0]
index=0
for i in range(napokdb):
    if bevetelek[i]<min:
        min=bevetelek[i]
        index=i
print('3. feladat: A legkisebb bevétel a listában itt található:',index,'és ennyi volt:',min,'Ft.')

#4. feladat
szum=0
for i in range(napokdb):
    szum+=bevetelek[i]
print('4. feladat: A teljes bevétel a hónapban:',szum,'Ft.')

#5. feladat
atlag=szum/napokdb
print('5. feladat: Az átlagos bevétel ennyi volt:',atlag,'Ft.')

#6. feladat
magas=28000
print('6. feladat: A listában ezeken a helyeken találtam magas bevételt:')
for i in range(napokdb):
    if bevetelek[i]>magas:
        print(i)

#7. feladat
alacsony=20000
print('7. feladat: A listában ezeken a helyeken találtam alacsony bevételt:')
for i in range(napokdb):
    if bevetelek[i]<alacsony:
        print(i)

#8. feladat
db20k=0
for i in range(napokdb):
    if bevetelek[i]>20000:
        db20k+=1
print('8. feladat:',db20k,'alkalommal volt nagyobb 20.000 Ft-tól a bevétel.')

#9. feladat

db20k=0
for i in range(napokdb):
    if bevetelek[i]<=20000:
        db20k+=1
print('9. feladat:',db20k,'alkalommal volt legfeljebb 20.000 Ft a bevétel.')

'''
egyszerűbb megoldás az előző helyett: 
print('9. feladat:',napokdb-db20k,'alkalommal volt legfeljebb 20.000 Ft a bevétel.')
'''
#10. feladat
kulonbseg=max-min
print('10. feladat: A legnagyobb és a legkisebb bevétel közötti különbség:',kulonbseg,'Ft.')

#11. feladat
print('11. feladat: A lista ezen értékei voltak a legstabilabbak:')
stabil=0
for i in range(napokdb):
    stabil=bevetelek[i]-atlag
    if -3000<=stabil<=3000:
        print(i)

#12. feladat
kulonbseg2=atlag-bevetelek[0]
index=0
if kulonbseg2<0:
    kulonbseg2*=(-1)
maxkul=kulonbseg2

for i in range(napokdb):
    kulonbseg2=atlag-bevetelek[i]
    if kulonbseg2<0:
        kulonbseg2*=(-1)
    if maxkul<kulonbseg2:
        maxkul=kulonbseg2
        index=i

print('12. feladat: A legjelentősebben itt tért el a bevétel az átlagtól:',index)

#13. feladat
alattadb=0
for i in range(napokdb):
    if bevetelek[i]<atlag:
        alattadb+=1
print('13. feladat: Ennyi alkalommal volt átlag alatti a bevétel:',alattadb)

#14. feladat
pont15k=0
for i in range(napokdb):
    if bevetelek[i]==15000:
        pont15k+=1
print('14. feladat: Ennyi alkalommal volt 15000 Ft a bevétel:',pont15k)

#15. feladat
for i in range(napokdb-1):
    if bevetelek[i]<bevetelek[i+1]:
        print('a bevétel javult')
    elif bevetelek[i]==bevetelek[i+1]:
        print('nem változott')
    else:
        print('a bevételt gyengült')

#16. feladat
szumma=0
for i in range(6,napokdb,7):
    szumma+=bevetelek[i]
for i in range(5,napokdb,7):
    szumma+=bevetelek[i]
print('A hétvégenként összesen ennyi bevételt: ',szumma)