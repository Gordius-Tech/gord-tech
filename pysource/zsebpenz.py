kiadasok = [1000, 1200, 0, 1500, 2000, 300, 0]
zsebpenz=6000

#1. feladat
szum=0
for i in range(7):
    szum+=kiadasok[i]
print('1. feladat: Az összes kiadásod:', szum)
if szum >6000:
    print('Nincs ennyi pénzed')

#2. feladat
db=0
for i in range(7):
    if kiadasok[i]==0:
        db+=1
print(f"2. feladat: Vilmos {db} nap nem költene semmit a zsebpénzéből")

#3. feladat
max=kiadasok[0]
index=0
for i in range(1,7):
    if max<kiadasok[i]:
        index=i
        max=kiadasok[i]
print(f'3. feladat: A legtöbb kiadás {max} Ft és a(z) {index+1} napon történne.')

#4. feladat
min=6001
index=None
for i in range(7):
    if min>kiadasok[i] and kiadasok[i]!=0:
        index=i
        min=kiadasok[i]
print(f'4. feladat: A legkevesebb kiadás {min} Ft és a(z) {index+1} napon történne.')

#5. feladat
print(f'5. feladat: Az tervezett napi átlagos költés {szum/7} Ft')

#6. feladat
print(f'6. feladat: Ennyi pénz maradna a kiadások után: {szum-zsebpenz}')

#7. feladat
ezrenfelul = []
for i in range(7):
    if kiadasok[i]>1000:
        ezrenfelul.append(kiadasok[i])
print(f'7. feladat: 1000 Ft fölötti költések: {ezrenfelul}.')

#8. feladat
duplalst= []
for i in range(7):
    duplalst.append(kiadasok[i]*2)
print(f'8. feladat: A kiadások megduplázva: {duplalst}.')

#9. feladat
hetkoz=hetveg=0
for i in range(0,5):
    hetkoz+=kiadasok[i]
    print(kiadasok[i])
for i in range(5,7):
    hetveg+=kiadasok[i]
print(f'9. feladat: Hétközbeni kiadások összesen: {hetkoz}, hétvégi kiadások összesen: {hetveg}.')

#10. feladat
for i in range(7):
    if kiadasok[i]==0:
        kiadasok[i]=500
print(f'10. feladat: az új napi kiadások a következők: {kiadasok}.')

#11. feladat
szum2=0
for i in range(7):
    szum2+=kiadasok[i]
hiany=szum2-szum
if hiany >0:
    print(f'11. feladat: Kölcsön kell kérnie Vilmosnak {hiany} Ft-ot.')
else:
    print('11. feladat: Nem kell köncsönkérnie Vilmosnak.')

#12. feladat
vissza=0
if hiany>0:
    print(f'12. feladat: Ennyit kell visszafizetni 10%-os kamat mellett: {hiany*1.1} Ft.')
else:
    print(f'12. feladat: Nem kell visszafizetni semmit.')

#13. feladat
print('13. feladat:')
for i in range(1,7):
    print(f'{i+1}. nap ennyivel változott a költés összege az előző naphoz képest {(kiadasok[i])-kiadasok[i-1]}.')

#14. feladat
print('14. feladat')
szum=atlag=0
for i in range(7):
    szum+=kiadasok[i]
atlag=szum/7
for i in range(7):
    if kiadasok[i]>atlag:
        print(f'{i+1}. több')
    elif kiadasok[i]<atlag:
        print(f'{i + 1}. kevesebb')
    else:
        print(f'{i + 1}. átlag')


