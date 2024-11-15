eladas=int(input('Hány Ft értékben adott el az eladó? '))
if eladas >10000:
    print('1000 Ft bónusz jár')
elif 10000 >=eladas >= 5000:
    print('500 Ft bónusz jár')
elif 5000 > eladas >= 0:
    print('Nincs bónusz')
else:
    print('Negatív számot nem lehet megadni')