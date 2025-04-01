from random import randint
print('O computador vai pensar em um número, e você precisa acertar, então faça suas tentativas: ')
tenta = int(input('>'))
dado = randint(0, 10)
qt = 1

while tenta != dado:
    if tenta < dado:
        print('Um pouco mais')
    elif tenta > dado:
        print('Um pouco menos')
    print('Faça outra tentativa: ')
    qt += 1
    tenta = int(input('>'))
print(f'Você acertou! O número era {dado}')
print(f'Você precisou de {qt} até acertar')