a = int(input('Digite um número: '))
b = int(input('Digite outro: '))
c = int(input('Mais um: '))
d = int(input('Último: '))
tutu = a, b, c, d

condi = False

noves = 0
for i in tutu:
    if i == 9:
        noves +=1
if noves > 0:
    print(f'O número 9 foi digitado {noves} vezes')
    condi = True
if a == 3 or b == 3 or c == 3 or d == 3:
    print(f'O primeiro 3 da lista está na posição {tutu.index(3)+1}')
    condi = True

ref = 0
for i in tutu:
    if i % 2 == 0:
        ref += 1
if ref > 0:
    print('Os números pares foram: ', end='')
    for i in tutu:
        if i % 2 == 0:
            print(f'{i} ', end='')
    condi = True
if not condi:
    print('Nenhuma das condições se aplica')