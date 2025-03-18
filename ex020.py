from random import choice, sample

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

lista = [al4, al3, al2, al1]

sorteio = sample(lista, 4)

print(f'A ordem sorteada para a apresentação é: {sorteio}')