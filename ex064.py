count = som = i = 0
print('Digite uma série de números: ')
while i != 999:
    count += 1
    som += i
    i = int(input('>'))
print(f'No fim, você digitou {count} números no total, e a soma entre eles foi de {som}')