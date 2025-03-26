from datetime import date
idade = date.today().year - int(input('Digite qual é o seu ano de nascimento: '))

print('Assim, a sua classificação na Confederação Nacional de Natação é \033[35m', end = '')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 20:
    print('Sênior')
elif idade > 20:
    print('Master')