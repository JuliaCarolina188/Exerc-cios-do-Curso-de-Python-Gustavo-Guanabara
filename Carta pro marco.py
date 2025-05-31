from time import sleep
from random import choice, randint
tempo = 1
frases = ('Te amo muito', 'Gosto muito de ti', 'Te admiro muito', 'Tu é incrível', 'Tu é perfeito',
          'Tu é inteligentíssimo', 'Passar tempo contigo é muito bom, Queria ter mais tempo contigo',
          'TU É LINDO DEMAIS', 'muito gostoso deus do céu', 'queria sentar em ti')
print(f'Oi vida!!!!')
sleep(tempo)
print(f'Só queria dizer..')
sleep(tempo)
print(f'que')
sleep(tempo)
print('Adivinha')
sleep(tempo)
print('Que eu te amo muito')
sleep(tempo)
print(f'E que', end='')
sleep(tempo)
print(f'.', end='')
sleep(tempo)
print(f'.', end='')
sleep(tempo)
print(f'.', end='')
sleep(tempo+1)

while True:
    print(f'\033[0m', end='')
    cor_texto = randint(0, 7)
    cor_fundo = randint(0, 7)

    while True:
        if cor_texto != 3 and cor_fundo != 3 and cor_texto != 7 and cor_fundo != 7 and cor_fundo != cor_texto:
            break
        cor_texto = randint(0, 7)
        cor_fundo = randint(0, 7)

    print(f'\033[3{cor_texto}m', end='')
    print(f'\033[4{cor_fundo}m', end='')
    print(f'\033[{cor_texto}m', end='')
    print(f'{choice(frases)}')
    sleep(tempo/6)