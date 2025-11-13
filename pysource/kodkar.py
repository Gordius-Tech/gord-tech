napitav = [412, 625, 378, 742, 589, 0, 655, 704, 498, 610, 275, 532]

#1. feladat
napdb=len(napitav)
print(f'1. feladat: a verseny {napdb} napig tartott.')

#2. feladat
ossz=0
for i in range(napdb):
    ossz+=napitav[i]
print(f'2. feladat: a versenyen {ossz} km-t tettek meg összesen.')

#3. feladat
pihidb=0
for i in range(napdb):
    if napitav[i]==0:
        pihidb+=1
print(f'3. feladat: összesen {pihidb} napot töltöttek pihenéssel.')

#4. feladat
gumicheck= ossz//200
print(f'4. feladat: összesen {gumicheck} alkalommal ellenőrizték a gumik állapotát.')

#5. feladat
max=napitav[0]
index=0
for i in range(napdb):
    if max<napitav[i]:
        max=napitav[i]
        index=i
print(f'5. feladat: A legtöbbet a(z): {index+1} napon tették meg, mégpedig {max} km-t.')

#6. feladat
min= 10000
index=None
for i in range(napdb):
    if min>napitav[i] and napitav[i]>0:
        min=napitav[i]
        index=i
print(f'6. feladat: A legkevesebbet a(z): {index+1} napon tették meg mégpedig {min} km-t.')

#7. feladat
aktivnapok=napdb-pihidb
atlag=ossz/aktivnapok
print(f'7. feladat: Átlagosan ennyi km-t tettek meg: {atlag:.2f}')

#8. feladat
feltav=ossz//2
km=0
for i in range(napdb):
    km+=napitav[i]
    if km>feltav:
        print(f'8. feladat: A(z) {i+1}. napon voltak túl a féltávon.')
        break

#9. feladat
print('9. feladat')
for i in range(napdb):
    if napitav[i]!=0:
        if atlag > napitav[i]:
            print('\tkevesebb')
        elif atlag == napitav[i]:
            print('\tátlag')
        else:
            print('\ttöbb')

#10. feladat
also=int(input('Add meg az alsó értéket: '))
felso=int(input('Add meg a felső értéket: '))
beluldb=0
for i in range(napdb):
    if napitav[i]>also and napitav[i]<felso and napitav[i]!=0:
        beluldb+=1
print(f'10. feladat: A két határértéken belül {beluldb} nap teljesítettek.')

#11. feladat
szombat=vasarnap=0
for i in range(napdb):
    if (i+1)%6==0:
        szombat+=napitav[i]

for i in range(napdb):
    if (i+1)%7==0:
        vasarnap+=napitav[i]
hetvege=szombat+vasarnap
print(f'11. feladat: Hétvégenként {hetvege} km-t tettek meg.')

#12. feladat
print('12. feladat: ezeken a napon (napokon) volt pihenő:')
for i in range(0, napdb, 7):
    if i < napdb and napitav[i] == 0:
        print('\tHétfő')
    if i + 1 < napdb and napitav[i + 1] == 0:
        print('\tKedd')
    if i + 2 < napdb and napitav[i + 2] == 0:
        print('\tSzerda')
    if i + 3 < napdb and napitav[i + 3] == 0:
        print('\tCsütörtök')
    if i + 4 < napdb and napitav[i + 4] == 0:
        print('\tPéntek')
    if i + 5 < napdb and napitav[i + 5] == 0:
        print('\tSzombat')
    if i + 6 < napdb and napitav[i + 6] == 0:
        print('\tVasárnap')

#13. feladat
szazalek=[]
print(f'13. feladat: A napi százalékos teljesítmény:')
for i in range(napdb):
    print((f'\t{i+1}.nap: {(napitav[i]/ossz)*100:.2f}'))

#14. feladat
print('14. feladat: ezeken a napokon 20% volt a teljesítményeltérés az átlaghoz képest')
pluszelteres=atlag*1.2
negelteres=atlag*0.8
for i in range(napdb):
    if not(negelteres<napitav[i]<pluszelteres):
        print(f'{i+1}. nap',end=' ')



