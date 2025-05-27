def fatorials(n, show=False):
    """fatorials(n, show=False)
    Essa função faz o cálculo fatorial de um número n.
    parâmetro show define se o cálculo será mostrado ou não"""
    fat = n
    print(f'{n} x ', end='' if show else '')
    for i in range(n-1, 1, -1):
        if show:
            print(f'{i} x ', end='')
        fat = fat * i
    print(f'1 = {fat}' if show else '')
    return fat

nu = int(input('Digite o número do fatorial: '))
ft_5 = fatorials(nu)
print(ft_5)