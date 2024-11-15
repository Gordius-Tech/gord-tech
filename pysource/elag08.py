hosorsz=int(input('Melyik hónapban vagyunk: '))
if hosorsz==1 or hosorsz==3 or hosorsz==5 or hosorsz==7 or hosorsz==8 or hosorsz==10 or hosorsz==12:
    print('A hónap 31 napos')
elif hosorsz==4 or hosorsz==6 or hosorsz==9 or hosorsz==11:
    print('A hónap 30 napos')
elif hosorsz==2:
    print('A hónap 28 vagy 29 napos attól függ, hogy szőkőév van e')
else:
    print('Rossz adatot adtál meg')
