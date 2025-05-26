infor = [{'nome':input('Nome do jogador: '), 'partidas':int(input('Quantidade de partidas jogadas: '))},
         {}]

for i in range(0, infor[0]['partidas']):
    infor[1][f'Jogo {i + 1}'] = int(input(f'   Gols na partida {i + 1}: '))

print('-'*30)
print(infor)
print('-'*30)

print('-'*30)
print(f'O jogador {infor[0]['nome']} fez:')
for i in infor[1]:
    print(f'No {i}, {infor[1][i]} gols')