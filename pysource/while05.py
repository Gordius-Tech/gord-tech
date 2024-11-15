szam = int(input('Kérek egy számot: '))
parosdb=paratlandb=0
while szam !=0:
    if szam%2==0:
        parosdb+=1
    else:
        paratlandb+=1
    szam = int(input('Kérek egy számot: '))
print('Ennyi számot adtunk meg összesen: ', parosdb+paratlandb, 'ebből páros: ',parosdb, 'ebből páratlan: ', paratlandb)

