szam=int(input('Melyik számot vizsgáljam? '))
osztdb=0
for i in range(1,szam+1):
    if szam%i==0:
        osztdb+=1
print('A(z) ',szam, ' számnak ', osztdb,'osztója van')