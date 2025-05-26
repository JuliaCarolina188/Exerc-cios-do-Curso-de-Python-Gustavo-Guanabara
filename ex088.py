from time import sleep
from random import randint
tigrinho = []
temp = []
print('-'*30)
print(f'{'TIGRINHO DA CAROLA':^30}')
print('-'*30)
quant = int(input('Fala meu querido, quantos jogos ai q tu quer sortear: '))
for i in range(0, quant):
    sleep(1)
    for s in range(0, 6):
        controle = randint(1, 60)
        while controle not in temp:
            controle = randint(1, 60)
        temp.append(controle)
    temp.sort()
    print(temp)
    tigrinho.append(temp[:])
    temp.clear()
r = input('Quer ver quantos jogo tu sorteou? ').lower()
while r not in 'sn':
    r = input('Quer ver quantos jogo tu sorteou? ').lower()
if r == 's':
    print(tigrinho)