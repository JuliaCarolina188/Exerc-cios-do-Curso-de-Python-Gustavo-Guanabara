boletins = []
temp = []
r = ''
id_ = maior_palavra = 0

while 'n' not in r:
    temp.append(id_)
    temp.append(input('Nome do aluno: ').strip().capitalize())
    temp.append(float(input('   Primeira nota: ')))
    temp.append(float(input('   Segunda nota: ')))
    temp.append((temp[2] + temp[3]) / 2)

    if temp[0] == 0:
        maior_palavra = len(temp[1])
    else:
        if len(temp[1]) > maior_palavra:
            maior_palavra = len(temp[1])

    boletins.append(temp[:])
    temp.clear()
    id_ += 1

    r = input('      Deseja continuar? ').lower().strip()

print(f'{'Id':_^6}{'Nome':_^{maior_palavra + 2}}{'Média':_^8}')
for i in boletins:
    print(f'{i[0]:^6}{i[1]:^{maior_palavra + 2}}{i[4]:^8}')

print('Números negativos para parar')
resp = int(input('De qual aluno(id) você deseja ver as notas completas? '))

while resp >= 0:
    if resp > len(boletins) - 1:
        while resp >= len(boletins):
            print('Número inválido')
            resp = int(input('De qual aluno(id) você deseja ver as notas completas? '))
    print(f'{'Id':_^6}{'Nome':_^{maior_palavra + 2}}{'Média':_^8}')
    print(f'{boletins[resp][0]:^6}{boletins[resp][1]:^{maior_palavra + 2}}{boletins[resp][4]:^8}')
    resp = int(input('De qual aluno(id) você deseja ver as notas completas? '))