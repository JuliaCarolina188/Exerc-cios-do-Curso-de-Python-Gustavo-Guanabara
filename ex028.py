from random import randint
dado = randint(0, 5)
guess = int(input('Tente adivinhar qual foi o número que o computador pensou, de 0 a 5: '))
print('VOCÊ ACERTOU!!' if guess == dado else 'Você errou <3')
print(f'O número era {dado}')