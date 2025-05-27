def maior(lista):
    maior = 0
    for i in lista:
        if i > maior:
            maior = i
    print(f'O maior número dessa lista é o {maior}')

lst = []
while True:
    lst.append(int(input('>')))
    r = input('   Deseja continuar? ').lower()
    while r not in 'ns':
        r = input('   Deseja continuar? ').lower()
    if 'n' in r:
        break

maior(lst)