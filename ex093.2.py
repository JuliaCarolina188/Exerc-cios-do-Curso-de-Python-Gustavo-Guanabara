jogador = {'nome':input('Nome do jogador: '), 'gols':[]}
partidas = []
parti = int(input(f'Quantias partidas {jogador['nome']} jogou? '))
for i in range(0, parti):
    partidas.append(int(input(f'   Quantos gols {jogador['nome']} fez na partida {i + 1}: ')))
jogador['gols'] = partidas[:]
jogador['total de gols'] = str(sum(partidas))
print('-'*30)
print(jogador)
print('-'*30)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')
print('-'*30)
print(f'O jogador {jogador['nome']} jogou {parti} partidas')
for índice, valor in enumerate(jogador['gols']):
    print(f'   => Na partida {índice + 1} fez {valor} gols')
print(f'Isso é um total de {jogador['total de gols']} gols')