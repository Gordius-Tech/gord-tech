psz=int(input('Hány pontot ért el a tanuló?'))
if 0<=psz<=49:
    print('Elégtelen')
elif 50<=psz<=59:
    print('Elégséges')
elif 60<=psz<=69:
    print('Közepes')
elif 70<=psz<=84:
    print('Jó')
elif 85<=psz<=100:
    print('Jeles')
else:
    print('Hibás pontszámot adtál meg')