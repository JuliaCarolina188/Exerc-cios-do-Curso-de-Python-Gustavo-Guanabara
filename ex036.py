valor_da_casa = float(input('Para efetuar a compra por favor digite o valor da casa: '))
salario = float(input('Agora o seu salário: '))
anos = int(input('Quantos anos o senhor vai pagar a casa: '))
meses = int(input('E em quantos meses: '))

parcelas = (anos*12)+meses
valor_da_parcela = valor_da_casa / parcelas

cores = {'roxo':'\033[35m', 'limpo':'\033[0m'}

print(f'Dessa forma, cada parcela custará {cores['roxo']}R${valor_da_parcela:.2f}{cores['limpo']}.')

if valor_da_parcela > (salario * 30) / 100:
    print(f'Infelizmente será impossível fazer essa conta, já que o valor de uma parcela é maior que {cores['roxo']}30%{cores['limpo']} do seu salário')
else:
    print('Será possível efetuar a conta')