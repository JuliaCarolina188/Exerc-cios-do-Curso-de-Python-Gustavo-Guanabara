count = som = i = 0
print('Digite uma série de números: ')
while True:
    i = int(input('>'))
    if i == 999:
        break
    count += 1
    som += i
print(f'No fim, você digitou {count} números no total, e a soma entre eles foi de {som}')