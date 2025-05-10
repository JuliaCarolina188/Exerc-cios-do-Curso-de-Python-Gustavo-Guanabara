times = 'Internacional', 'Corinthians', 'Ceará', 'Fortaleza', 'Botafogo', 'Flamengo', 'Palmeiras', 'Chapecoense', 'Fluminense', 'Grêmio', 'Vasco', 'Cruzeiro', 'Bahia', 'São Paulo', 'Bragantino', 'Santos', 'Mirassol', 'Sport', 'Atlético-MG', 'Vitória'
print(f'Os 5 primeiros times são: {times[0:5]}')
print(f'Os 4 últimos são: {times[-4:]}')
print('Esses são os times em ordem alfabética: ')
print(sorted(times))
print(f'O Chapecoense está na posição {times.index('Chapecoense')+1}')