n = int(input('Adja meg az "n" értékét: '))
fakt=1
for _ in range(1,n+1):
    fakt*=_
print(n, ' faktoriálisa: ',fakt)
