grupo = []
pessoas = []
mai = []
men = []
while True:

    pessoas.append(input('Digite o nome dessa pessoa: '))
    pessoas.append(float(input('Digite o peso dessa pessoa: ')))

    if len(grupo) == 0:
        mai = pessoas[:]
        men = pessoas[:]
    else:
        if pessoas[1] > mai[1]:
            mai = pessoas[:]
        if pessoas[1] < men[1]:
            men = pessoas[:]

    grupo.append(pessoas[:])
    pessoas.clear()

    r = input('   Continuar(s/n)? ').lower()
    while r not in 'sn':
        r = input('   Continuar(s/n)? ').lower()
    if r == 'n':
        break

print(f'''Um total de {len(grupo)} pessoas foram cadastradas
A pessoa mais pesada foi {mai[0]} com {mai[1]}Kg
A pessoa mais leve foi {men[0]} com {men[1]}Kg
''')
print(f'A pessoa mais pesada foi {mai[0]} com {mai[1]}Kg, seguida por: ')
for i in grupo:
    if i == mai:
        print(end='')
    elif i[1] > mai[1] - 10:
        print(f'{i[0]}, com {i[1]}Kg')

print(f'A pessoa mais leve foi {men[0]} com {men[1]}Kg, seguida por: ')
for i in grupo:
    if i == men:
        print(end='')
    elif i[1] < men[1] + 10:
        print(f'{i[0]}, com {i[1]}Kg')