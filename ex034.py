salario = int(input('Digite seu salário: '))
print(f'Você receberá um aumento de \033[35m15%\033[0m, ficando com \033[35m{((salario*15)/100)+salario:.2f}R$\033[0m' if salario < 1251 else f'Você receberá um aumento de \033[35m10%\033[m, ficando com \033[35mR${((salario*10)/100)+salario:.2f}\033[m')