jojelszo='Titkos'
jelszo=input('Kérem a jelszót:')
tippdb=1
while jojelszo!=jelszo:
    jelszo = input('Kérem a jelszót:')
    tippdb+=1
print(tippdb, ' tippelés után találtad el a jelszót')
