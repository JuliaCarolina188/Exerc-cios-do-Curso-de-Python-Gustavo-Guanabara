n = int(input('Digite um número: '))
tot = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[35m', end='')
        tot = tot + 1
    else:
        print('\033[0m', end='')
    print(f'{i}, \033[0m',end='')
if tot > 2:
    print("\nO número não é primo")
else:
    print("\nO número é primo")