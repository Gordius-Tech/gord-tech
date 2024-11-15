a=int(input('Kérem az A oldal hosszát: '))
b=int(input('Kérem a B oldalt hosszát: '))
c=int(input('Kérem a C oldalt hosszát: '))
if a+b>c and a+c>b and b+c>a:
    print('Szerkeszthető')
else:
    print('Nem szerkeszthető')
    
