ho = int(input('Kérem a hónap sorszámát: '))
if (ho >=3) and (ho<=5):
    print('Tavasz van')
elif (ho>=6) and (ho<=8):
    print('Nyár van')
elif (ho>=9) and (ho<=11):
    print('Ősz van')
elif (ho==12) or (ho==1) or (ho==2):
    print('Tél van')
else:
    print('Hibás adatot adtál meg')
