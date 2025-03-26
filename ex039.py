from datetime import date
idade = date.today().year - int(input('Digite o ano em que você nasceu: '))

if idade < 18:
    print('Você ainda terá que se alistar no exército')
    print('Você terá que se alistar em ', end='')
    if 18 - idade ==  1:
        print('1 ano')
    else:
        print(f'{18 - idade} anos')
    print(f'Seu alistamento será em {date.today().year + (18 - idade)}')
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou da hora de você se alistar. Se tu já se alistou ou não aí eu já não sei')
    print(f'Dito isso, já se passou {idade - 18} anos desde que tu devia ter se alistado, ou seja, em {date.today().year - (idade - 18)}')
