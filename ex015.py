dias = int(input('Por quanto dias você alugou o carro? '))
km = float(input('Quantos quilômetros você rodou com ele? '))

preco = (60 * dias)+(0.15 * km)

print(f'No total, você terá que pagar R${preco:.2f}')