szam1=int(input('Kérem az első számot: '))
szam2=int(input('Kérem a második számot: '))
if szam1 < szam2:
    print('Növekvő sorrend: ',szam1,szam2)
elif szam1 > szam2:
    print('Növekvő sorrend: ', szam2,szam1)
else:
    print('A két szám egyenlő!')
