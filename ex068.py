from random import choice, randint
from time import sleep
vit = 0
print('''As regras são as seguintes:
Você terá que escolher entre impar ou par. O computador ficará com o que sobrar.
Você terá que digitar um número, e o computador dirá outro
A soma dos números decidirá o ganhador, sendo par ou ímpar''')
while True:
    print('-'*30)
    while True:
        print('Escolha entre impar(i) ou par(p): ')
        ioup = input('>').lower()
        if ioup == 'i' or ioup == 'p':
            break
    while True:
        print('Digite um número de 1 a 10:  ')
        n = int(input('>'))
        if 1 <= n <= 10:
            break
    ncompt = randint(1, 10)
    result = n + ncompt
    print('O computador escolhe')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print(f'{ncompt}!')

    if result % 2 == 0:
        print(f'{n} + {ncompt} = {n+ncompt}, que é par')
        if ioup == 'p':
            print('Você ganhou! + uma vitória para a conta. Próxima rodada: ')
            vit += 1
        else:
            print('Você perdeu...')
            break
    else:
        print(f'{n} + {ncompt} = {n + ncompt}, que é impar')
        if ioup == 'i':
            print('Você ganhou! + uma vitória para a conta. Próxima rodada: ')
            vit += 1
        else:
            print('Você perdeu...')
            break
if vit == 0:
    print('Você não venceu nenhuma vez.')
elif vit == 1:
    print('Você venceu 1 vez!')
else:
    print(f'Sua sequência de vitórias foi de {vit} vitórias seguidas!')