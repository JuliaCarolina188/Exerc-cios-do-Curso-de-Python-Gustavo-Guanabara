from random import choice
cores = {'roxo':'\033[32m', 'limpo':'\033[0m'}

op = ['pedra', 'papel', 'tesoura']
b = choice(op)
empate = False

a = input('pedra, papel ou tesoura? ').lower()

print(f'O computador escolheu... {cores['roxo']}{b}!{cores['limpo']}', end='')

if b == a:
    print(f'{b}! EMPATE!')
elif (a == 'tesoura' and b == 'papel') or (a == 'papel' and b == 'pedra') or (a == 'pedra' and b == 'tesoura'):
    print(f' Você venceu')
else:
    print(f' Você perdeu')