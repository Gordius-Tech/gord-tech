kod='adabbccdcababdcddcaaaxd'

#1. feladat
hossz=len(kod)
hiba=0
for i in range(hossz):
    if kod[i]!='a' and kod[i]!='b' and kod[i]!='c' and kod[i]!='d':
        hiba+=1
print('1. feladat')
if hiba>0:
    print(f'Összesen {hiba} hibás állapotjelölő kódot találtam.')
else:
    print('Nem találtam hibás állapotjelölő kódot.')

#2. feladat
#karaktercserét összfűzéssel oldottam meg olyat nem tudunk hogy kod[i]='d'
for i in range(hossz):
    if kod[i]!='a' and kod[i]!='b' and kod[i]!='c' and kod[i]!='d':
        kod=kod[:i]+'d'+kod[i+1:]
print('2. feladat')
print(f'Az aktuális állapotkód: {kod}')

#3. feladat
print('3. feladat')
print(f'A méhészetben {hossz} db kaptár van.')

#4. feldat
print('4. feladat')
adb=bdb=cdb=ddb=0
for i in range(hossz):
    if kod[i]=='a':
        adb+=1
    if kod[i]=='b':
        bdb+=1
    if kod[i]=='c':
        cdb+=1
    if kod[i]=='d':
        ddb+=1
print(f'Tökéletes kaptár száma: {adb}')
print(f'Kicsit hibás kaptár száma: {bdb}')
print(f'Közepesen hibás kaptár száma: {cdb}')
print(f'Teljesen hibás kaptár száma: {ddb}')

#5. feladat
print('5. feladat')
szum=0
for i in range(hossz):
    if kod[i]=='a':
        szum+=0
    if kod[i]=='b':
        szum+=1
    if kod[i]=='c':
        szum+=2
    if kod[i]=='d':
        szum+=3
atlag=szum/hossz
print(f'A kaptárak átlagos pontértéke: {atlag}.')

#6. feladat
print('6. feladat')
if atlag<1.0:
    print('A kaptárok általános állapota jó.')
elif atlag>2.0:
    print('A kaptárok állapota rossz.')
else:
    print('A kaptárok állapota közepes.')

#7. feladat
print('7. feladat')
print('Cserélni kell ezekeet a kaptárakat: ',end=' ')
for i in range(hossz):
    if kod[i]=='d':
        print(i+1,end=' ')

#8. feladat'

print('\n8. feladat')
print(f'A kaptárok {(ddb/hossz)*100:.2f}%-át kell cserélni.')

#9. feladat
print('9. feladat')
print(f"Javítások nélkül jövőre {cdb+ddb} kaptár lesz használhatatlan.")

#10. feladat
print('10. feladat')
akcios=ddb//5
if akcios >0:
    print(f'Összesen {akcios} db kaptár ára lesz akciós.')
else:
    print('Nem kap engedményt a méhész.')

#11. feladat
print('11. feladat')
koltseg=0
koltseg=adb*5000
koltseg+=bdb*10000
koltseg+=cdb*15000
teljesaru=ddb-akcios
koltseg+=teljesaru*30000
koltseg+=(akcios*30000)*0.85
print(f'A tervezett jvítási költség {koltseg} Ft.')

#12. feladat
print('12. feladat')
haszon=hossz*55000 #családonként 55ezer haszonnal számolunk
print(f'Év végére a teljes haszon {haszon-koltseg} Ft lesz.')


