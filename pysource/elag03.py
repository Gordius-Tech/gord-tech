kor = int(input('Hány éves vagy? '))
if (kor>=0) and (kor<=12):
    print('Gyermek')
elif (kor>=13) and (kor<=19):
    print('Tinédzser')
elif (kor>=20) and (kor<=64):
    print('Felnőtt')
elif kor>=65:
    print('Idős')
else:
    print('Hibás kort adtál meg')
