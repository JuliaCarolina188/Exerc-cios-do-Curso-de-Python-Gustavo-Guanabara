print(f'{'BANCO ANTHONY MARCOUS':-^40}')
n = int(input('Digite quanto dinheiro que você quer sacar do caixa: R$'))
while True:
    quantas_notas_50 = n // 50
    rest_div_50 = n % 50

    quantas_notas_20 = rest_div_50 // 20
    rest_div_20 = rest_div_50 % 20

    quantas_notas_10 = rest_div_20 // 10
    rest_div_10 = rest_div_20 % 10

    quantas_notas_1 = rest_div_10 // 1

    break
print(f'{'Valor da nota':-^20}{'Quantidade':-^15}')
print(f"{'50':^18}{quantas_notas_50:^15}" if quantas_notas_50 > 0 else '', end='')
print(f"\n{'20':^18}{quantas_notas_20:^15}" if quantas_notas_20 > 0 else  '', end='')
print(f"\n{'10':^18}{quantas_notas_10:^15}" if quantas_notas_10 > 0 else  '', end='')
print(f"\n{'1':^18}{quantas_notas_1:^15}" if quantas_notas_1 > 0 else '', end='')