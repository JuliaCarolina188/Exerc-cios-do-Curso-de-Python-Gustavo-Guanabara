from random import choice
cores = {'roxo':'\033[32m', 'limpo':'\033[0m'}

op = ['ganhar', 'empatar']
b = choice(op)

a = input('pedra, papel ou tesoura? ').lower()

print(f'O computador escolheu... {cores['roxo']}', end='')

if b == 'empatar':
    print(f'{a}{cores['limpo']}... infelizmente houve um empate')

elif b == 'ganhar':
    if a == 'tesoura':
        print('Pedra', end='')
    elif a == 'pedra':
        print('Papel', end='')
    elif a == 'papel':
        print('Tesoura', end='')
    print(f'{cores['limpo']}! O que faz com que ele tenha vencido')
else:
    print()