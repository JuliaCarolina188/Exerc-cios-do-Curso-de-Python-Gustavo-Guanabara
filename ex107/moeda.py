def dobro(n = 0, moedas = True):
    res = n * 2
    return res if not moedas else moeda(res)

def metade(n=0, moedas=True):
    res = float(n) / 2
    return res if not moedas else moeda(res)

def aumentar(n = 0, t = 0, moedas = True):
    res = n + ((n * t) / 100)
    return res if not moedas else moeda(res)

def diminuir(n = 0, t = 0, moedas = True):
    res = n - ((n * t) / 100)
    return res if not moedas else moeda(res)

def moeda(n = 0, sinal = 'R$'):
    return f'{sinal}{float(n):>.2f}'.replace('.', ',')

def resumo(n, at, dt):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'{'Valor analisado':20}{moeda(n):>20}')
    print(f'{'Dobro do valor':20}{dobro(n):>20}')
    print(f'{'Metade do valor':20}{metade(n):>20}')
    print(f'{f'+{at}% do valor':20}{aumentar(n, at):>20}')
    print(f'{f'-{dt}% do valor':20}{diminuir(n, dt):>20}')
    print('-' * 40)