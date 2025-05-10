frase = input('Digite uma frase: ')
tutu = frase.split()
print(f'{'Quantas vogais há?':-^35}')
for c in range(len(tutu)):
    print('\033[0m', end='')
    print(tutu[c] + ': ', end='')
    for i in tutu[c]:
            print('\033[35m', end='')
            if i in 'aeiou':
                print(f'\033[35m{i} ', end='')
            else:
                print(f'\033[0m{i} ', end='')
    print()