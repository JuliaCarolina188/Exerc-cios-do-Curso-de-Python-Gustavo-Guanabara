soma = 0
contador = 0
for c in range(1, 501, 2):
    print(c)
    if c % 3 == 0:
        soma = soma + c
        contador = contador + 1
print(f'A soma de todos os {contador} números ímpares, múltiplos de 3, de 1 a 500, é de \033[35m{soma}')