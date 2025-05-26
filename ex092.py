from datetime import date
inf = {'Nome':input('Digite seu nome: '),
       'Idade':date.today().year - int(input('Digite o seu ano de nascimento: ')),
       'Ctps':int(input('Digite o número da carteira de trabalho. 0 caso não tenha: '))}
if inf['Ctps'] != 0:
    inf['Ano de contratação'] = int(input('Digite seu ano de contratação: '))
    inf['Salario'] = int(input('Digite seu salário: '))
    inf['Aposentadoria'] = inf['Idade'] + ((inf['Ano de contratação'] + 35) - date.today().year)
    for key, value in inf.items():
        print(f'{key}: {value}')
else:
    print(inf)