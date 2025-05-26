print('''
    0   1   2
0   x   x   x
1   x   x   x
2   x   x   x''')
print('Preencha a seguinte matriz: ')
matriz = [[0, 0, 0,], [0, 0, 0,], [0, 0, 0,]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'{linha}, {coluna}>'))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}] ', end='')
    print()