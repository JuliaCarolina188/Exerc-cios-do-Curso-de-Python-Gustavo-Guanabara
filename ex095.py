time = []
jogador = {}
gols = []

while True:
    jogador['código'] = len(time)
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input(f'Quantas partidas {jogador['nome']} jogou no campeonato: '))

    for i in range(0, jogador['partidas']):
        gols.append(int(input(f'   Quantos gols {jogador['nome']} fez na partida {i + 1}: ')))

    jogador['gols'] = gols[:]
    jogador['soma'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()

    r = input('      Deseja continuar? ')
    while r not in 'sn':
        r = input('      Deseja continuar? ')
    if 'n' in r:
        break

print('-'*50)
print(f'{'Código':_^7}{'Nome':_^8}{'Partidas':_^12}{'Gols':_^10}{'Soma':_^7}')
for i in time:
    print(f'{i['código']:^7}{i['nome']:^8}{i['partidas']:^12}{str(i['gols']):^10}{i['soma']:^7}')

while True:
    while True:
        codigo = int(input('Digite o nome do jogador que deseja saber as informações sobre(- para parar): '))
        if codigo <= len(time) - 1:
            break
    if codigo < 0:
        break
    print(f'{f'LEVANTAMENTO DO JOGADOR {time[codigo]['nome']}'}')
    for indice, valor in enumerate(time[codigo]['gols']):
        print(f'No jogo {indice+1}, {valor} gols')