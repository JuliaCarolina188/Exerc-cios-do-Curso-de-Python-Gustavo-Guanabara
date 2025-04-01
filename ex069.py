ref = 1
maiores = qhomens = mumenid = 0
while True:
    print('-'*30)
    print(f'Informações sobre a {ref}ª pessoa')
    sex = input('Qual é o sexo dessa pessoa(f/m)? ')
    while True:
        if sex == 'f' or sex == 'm':
            break
        print('Por favor escolha um sexo válido, f ou m: ')
        sex = input('>')
    idade = int(input('Qual é a idade dessa pessoa? '))
    while True:
        if 115> idade > 0:
            break
        print(f'Por favor escolha uma idade válida, positiva e menor que 115: ')
        sex = input('>')
    ref += 1

    if idade >= 18:
        maiores += 1
    if sex == 'm':
        qhomens =+ 1
    elif sex == 'f' and idade < 18:
        mumenid += 1

    q = input('Você quer continuar(n/s)? ')
    if q == 'n':
        break
print(f'No fim, houveram: ')
print(f'{maiores} pessoas com maiores de idade')
print(f'{qhomens} homens cadastrados')
print(f'{mumenid} mulheres menores de idade cadastradas')