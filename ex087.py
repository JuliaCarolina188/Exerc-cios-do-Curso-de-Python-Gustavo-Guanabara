print('''
    0   1   2
0   x   x   x
1   x   x   x
2   x   x   x''')
print('Preencha a seguinte matriz: ')
matriz = [[0, 0, 0,], [0, 0, 0,], [0, 0, 0,]]
soma_pares = soma_3_coluna = soma_2_linha =0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'{linha}, {coluna}>'))

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_3_coluna += matriz[linha][coluna]
        if linha == 1:
            soma_2_linha += matriz[linha][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^3}] ', end='')
    print()
print(f'''A soma de todos os números pares é de: {soma_pares}
A soma dos números da 3ª coluna é igual a: {soma_3_coluna}
A soma dos números da segunda linha é igual a: {soma_2_linha}''')