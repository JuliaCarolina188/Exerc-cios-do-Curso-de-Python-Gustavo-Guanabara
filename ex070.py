print(f'{'LOJA DO SUPER BARATÃO':-^40}')
ref = 1
total = maior_q_1000 = 0
str_mais_barato = ''
int_mais_barato = float('inf')

while True:
    print(f'{ref}º produto:')
    nome = input('  Digite o nome do produto: ')
    preco = float(input('  Digite seu preço: R$'))
    q = input('Você quer continuar(s/n)? ')

    total += preco
    if preco >= 1000:
        maior_q_1000 += 1
    if q == 'n':
        break
    if preco < int_mais_barato:
        int_mais_barato = preco
        str_mais_barato = nome
    ref += 1
print(f'O total que você gastou aqui foi de R${total:.2f}')
print(f'Você comprou {maior_q_1000} itens que custavam mais que R$1000.00')
print(f'O produto mais barato foi {str_mais_barato}')