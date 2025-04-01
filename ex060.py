fat = n = ref = int(input('Digite um número para calcular seu fatorial: '))
print(f'{n}! = ', end='')
while ref != 1:
    print(f'{ref} x ', end='')
    ref = ref - 1
    fat = fat * ref
print(f'1 = {fat}')