dobasok = [3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4 ]
poz = 0
db=0

print('2. feladat')
for i in range(len(dobasok)):
    poz+=dobasok[i]
    if poz%10==0:
        poz-=3
        db+=1
    print(poz, end=' ')
print()

print('3. feladat')
print(f'A játék során {db} alkalommal lépett létrára.')

print('4. feladat')
if poz>=45:
    print('A játékot befejezte.')
else:
    print('A játékot elhagyta.')