from random import randint

def sorteia(lista, quantidade):
    """
    Adiciona uma determinada quantidade de números sorteados em uma lista.
    Essa quantidade é definida pelo segundo argumento, enquanto a lista onde esses
    números serão adicionados é definida pelo primeiro argumento
    """
    for i in range(0, quantidade):
        temp = randint(0, 100)
        print(f'{temp} ', end='')
        lista.append(temp)

def soma_par(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'\nA soma dos números pares dessa lista é igual a {soma}')

help(sorteia)
nums = []
sorteia(nums, 5)
soma_par(nums)