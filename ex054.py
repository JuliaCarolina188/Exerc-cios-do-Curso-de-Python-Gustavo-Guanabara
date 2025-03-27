from datetime import date
maiores = minors = 0
print('Digite o ano de nascimento de 7 pessoas: ')
for i in range(0, 7):
    a = date.today().year - int(input('>'))
    if 17 >= a:
        minors = minors + 1
    else:
        maiores = maiores + 1
print(f'''Quantidade de pessoas maiores de idade: {maiores}
Quantidade de pessoas menores de idade: {minors}''')