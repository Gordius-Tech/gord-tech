a=0
b=1
fibdb=2
print('A(z) 1 . fibonacci szám a(z): 0')
print('A(z) 2 . fibonacci szám a(z): 1')
while fibdb<10:
    c=a+b
    a=b
    b=c
    fibdb+=1
    print('A(z)' ,fibdb,'. fibonacci szám a(z):', c)