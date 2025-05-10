print('Digite 5 números: ')
lista = []
for i in range(0, 5):
    lista.append(int(input('>')))

lista_ordenada = []
for i in range(0, len(lista)):
    lista_ordenada.append(min(lista))
    del lista[lista.index(min(lista))]

print('A lista ordenada fica: ')
for i in lista_ordenada:
    if i == min(lista_ordenada):
        print(f'{i}', end='')
    else:
        print(f', {i}', end='')