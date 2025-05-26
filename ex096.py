def mostra_linha(a, b):
    print('-'*40)
    print(f'{f'{a} + {b} = {a+b}':^40}')
    print('-' * 40)

a = int(input())
b = int(input())
mostra_linha(a, b)
