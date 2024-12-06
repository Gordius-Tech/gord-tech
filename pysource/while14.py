megfejtes = 5
tipp=int(input('Melyik számra gondoltam? '))
tippdb=1
while tipp!=megfejtes:
    tippdb+=1
    if megfejtes >tipp:
        tipp=int(input('Nagyobb számra gondoltam: '))
    else:
        tipp=int(input('Kisebb számra gondoltam: '))
print('Vége a játéknak. Tippek száma: ',tippdb)