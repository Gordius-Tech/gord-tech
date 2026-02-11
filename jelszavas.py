import random
import string

kisbetuk=string.ascii_lowercase
nagybetuk=string.ascii_uppercase
szamok=string.digits
egyeb=string.punctuation

jelszo=[]

#a jelszó hosszának megadása
hossz=int(input('Hány karakter hosszú legyen a jelszó (mininum 4 legyen)? '))
if hossz<4:
    print('Hibás adat')
    exit()

#megállapítjuk hány kisbetű, nagybetű, szám, egyéb karakerből álljon a program
kisb_szama=random.randint(1,hossz-3) #azért -3 mert úgy gondolkodunk minden fajta karakterből lesz benne legalább 1
#print(kisb_szama)
hossz-=kisb_szama
nagyb_szama=random.randint(1, hossz-2)
#print(nagyb_szama)
hossz-=nagyb_szama
szamok_szama=random.randint(1,hossz-1)
#print(szamok_szama)
hossz-=szamok_szama
egyeb_szama=hossz
#print(egyeb_szama)

for i in range(kisb_szama):
    poz=random.randint(0,len(kisbetuk)-1)
    jelszo.append(kisbetuk[poz])

for i in range(nagyb_szama):
    poz=random.randint(0,len(nagybetuk)-1)
    jelszo.append(nagybetuk[poz])

for i in range(szamok_szama):
    poz=random.randint(0,len(szamok)-1)
    jelszo.append(szamok[poz])

for i in range(egyeb_szama):
    poz=random.randint(0,len(egyeb)-1)
    jelszo.append(egyeb[poz])

random.shuffle(jelszo)

keszjelszo=''
for i in range(len(jelszo)):
    keszjelszo+=jelszo[i]

print(f'Egy ajánlott jelszó: {keszjelszo}')



