from random import choice

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

lista = [al4, al3, al2, al1]

sorteio = choice(lista)

print(f'O aluno sorteado foi {sorteio}')