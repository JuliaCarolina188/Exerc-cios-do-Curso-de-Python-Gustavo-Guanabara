lista = []
print('Digite 5 números')
for i in range(0, 5):
    n = int(input('>'))
    if i == 0 or n > lista[len(lista) - 1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1
print('A lista digitada em ordem é: ')
for i in range(len(lista)):
    if i == len(lista) - 1:
        print(f'{lista[i]}.')
    else:
        print(f'{lista[i]}, ', end='')