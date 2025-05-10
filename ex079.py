checagem = False
valor = []
print('Digite uma série de números. Para parar, é só digitar uma letra')
while True:
    n = input('>')
    if n.isalpha():
        break
    for i in valor:
        if i == int(n):
            print('Ja foi digitado')
            checagem = True
    if not checagem:
        valor.append(int(n))
    checagem = False
print(f'A lista digitada foi a seguinte: ')
valor.sort()
for i in valor:
    print(f'{i}, ', end='')
