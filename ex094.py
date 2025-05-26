pessoa = {}
grupo = []
idades = []
contador = 0
while True:
    print(f'Pessoa número {contador}')
    pessoa['nome'] = input('   Nome dessa pessoa: ')
    pessoa['sexo'] = input('   Sexo dessa pessoa(f/m): ').lower()
    while pessoa['sexo'] not in 'fm':
        pessoa['sexo'] = input('   Sexo dessa pessoa(f/m): ').lower()
    pessoa['idade'] = int(input('   Idade: '))
    contador += 1

    idades.append(pessoa['idade'])
    grupo.append(pessoa.copy())

    r = input('      Deseja continuar? ')
    while r not in 'sn':
        r = input('      Deseja continuar? ')
    if 'n' in r:
        break

media = float(sum(idades)) / float(len(idades))

print('-'*30, f'\nA) No total, {len(grupo)} pessoas foram cadastradas')
print(f'B) A média das idades foi de {media}')
print('B) as mulheres cadastradas foram: ')
for i in grupo:
    if i['sexo'] == 'f':
        print(i['nome'], end='')
print(f'\nD) Pessoas acima da média de idade foram: ')
for i in grupo:
    if i['idade'] >= media:
        for key, value in i.items():
            print(f'{key} = {value}; ', end='')
        print()