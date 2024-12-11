szoveg="helló"
tippdb=0
while input("Melyik szóra gondoltam? ") !=szoveg:
    tippdb+=1
    if tippdb==5:
        break
if tippdb<5:
    print('Gratulálok eltaláltad!')
else:
    print('Sajnos nem találtad el')