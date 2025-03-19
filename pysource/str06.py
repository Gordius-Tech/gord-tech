s1= input('Első szöveg: ')
s2= input('Második szöveg: ')
l1=len(s1)
l2=len(s2)
if l1>l2:
    print('Az első szó a hosszabb, ami összesen ',l1,' karakterből áll.')
    print('Az első szó ',l1-l2,' karakterrel hosszabb a másodiknál.')
elif l2>l1:
    print('A második szó a hosszabb, ami összesen ',l2,' karakterből áll.')
    print('A második szó ',l2-l1,' karakterrel hosszabb az elsőnél.')
else:
    print('A két szó egyforma hosszúságú.')