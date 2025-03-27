nome = ''
idade = soma = 0
maisvelho = ''
gen = ''
idadedomaisvelho = 0
mcommenosde20anos = 0
for i in range(1, 5):
    nome = input(f'Digite o nome da {i}ª pessoa: ')
    gen = input('Essa pessoa é homem(h) ou mulher(m)? ')
    idade = int(input('Essa pessoa tem quantos anos? '))

    soma = soma + idade
    if gen == 'h':
        if i == 1:
            maisvelho = nome
            idadedomaisvelho = idade
        if idade > idadedomaisvelho:
            idadedomaisvelho = idade
            maisvelho = nome
    elif gen == 'm':
        if idade <= 19:
            mcommenosde20anos = mcommenosde20anos + 1
    print('-'*20)
print(f'A média da idade do grupo é de {soma/4} anos')
print(f'O homem mais velho foi o {maisvelho}, com {idadedomaisvelho} anos')
print(f'A quantidade de mulheres que tem menos de 20 anos é de {mcommenosde20anos} mulheres')