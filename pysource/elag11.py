szam=int(input('Kérek egy számot: '))
if szam%3==0 and szam%5==0:
    print('A szám osztható 3-al és 5-el')
elif szam%3==0:
    print('A szám osztható 3-al')
elif szam%5==0:
    print('A szám osztható 5-el')
else:
    print('A szám nem osztható 3-al és 5-el sem.')
