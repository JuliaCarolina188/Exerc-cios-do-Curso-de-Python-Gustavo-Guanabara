preco = float(input('Qual é o preço normal do produto? '))
cores = {'roxo':'\033[32m', 'limpo':'\033[0m'}
print(f'''Digite o número da forma de pagamento: 
1. a vista: {cores['roxo']}10%{cores['limpo']} de desconto
2. a vista no cartão: {cores['roxo']}5%{cores['limpo']} de desconto
3. em até 2x no cartão: {cores['roxo']}preço normal{cores['limpo']}
4. 3x ou mais no cartão: {cores['roxo']}20%{cores['limpo']} de juros''')
condi = input('>')
if condi == '1':
    print(f'O preço do produto fica {cores['roxo']}R${preco - (preco*10)/100:.2f}')
elif condi == '2':
    print(f'O preço do produto fica {cores['roxo']}R${preco - (preco*5)/100:.2f}')
elif condi == '3':
    print(f'O preço do produto fica {cores['roxo']}R${preco:.2f}{cores['limpo']}, que é o preço normal')
elif condi == '4':
    print(f'O preço do produto fica {cores['roxo']}R${preco + (preco * 20) / 100}{cores['limpo']}')
else:
    print(f'Esse número é inválido, então o preço vai de {cores['roxo']}R${preco:.2f}{cores['limpo']} pra {cores['roxo']}R$983203.00')