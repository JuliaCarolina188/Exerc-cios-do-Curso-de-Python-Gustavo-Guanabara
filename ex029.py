km = int(input('Há quantos quilômetros você está andando agora? '))
cores = {'roxo':'\033[035m', 'limpo':'\033[0m'}
if km <= 80:
    print('Tudo certo por aqui')
else:
    print(f'Infelizmente teremos que estar multando o senhor aí em {cores['roxo']}7R${cores['limpo']} ao quilômetro cima do limite de velocidade, que é {cores['roxo']}80km/h{cores['limpo']}')
    print(f'A multa é igual a {cores['roxo']}{(km-80)*7}R${cores['limpo']}')