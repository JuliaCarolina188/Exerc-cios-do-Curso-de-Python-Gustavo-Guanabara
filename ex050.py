s = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s = s + num
print(f'A soma dos números pares digitados é de {s}')