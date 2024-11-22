szam = int(input('Meddig írjam ki a számokat? '))
kezd=1
if szam>0:
    while szam>=kezd:
        print(kezd)
        kezd+=1
else:
    print('A megadott szám nem megfelelő vagy negatív vagy 0')
