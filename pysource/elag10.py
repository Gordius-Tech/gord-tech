felh='admin'
jelszo='titkos'
befelh=input('Kérem a felhasználói nevedet: ')
bejelszo=input('Kérem a jelszavadat: ')
if befelh==felh and bejelszo==jelszo:
    print('Sikeres bejelentkezés')
else:
    print('Hibás adatok')