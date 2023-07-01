print('capivaras')

a = int(input('Insira número:'))
for i in range(1, a+1):
    if (i == 1):
        print(i,'capivara não incomoda ninguem')
    elif i%2 == 0:
        x = 'incomodam '*i
        print(i,'capivaras',x,'muito menos')
    else:
        print(i,'capivaras não incomodam ninguem')
