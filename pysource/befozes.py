uvegek=[5, 2, 2, 4, 3, 2, 4, 10, 5, 5, 3, 5, 4, 3, 3 ]

print('2. feladat')

dl=0
while not(0<dl<200):
    dl=int(input('Mari néni lekvárja (dl): '))

print('3. feladat')
index=0
max=uvegek[0]
for i in range(len(uvegek)):
    if max<uvegek[i]:
        max=uvegek[i]
        index=i
print(f'A legnagyobb üveg {max} dl és {index+1}. a sorban.')

print('4. feladat')
szum=0
for i in range(len(uvegek)):
    szum+=uvegek[i]

if szum> dl:
    print('Marad lekvár.')
else:
    print('Elegendő üveg volt.')