def info(jogador='<desconhecido>', gols='0'):
    if jogador.strip() == '':
        jogador = '<desconhecido>'
    if gols.strip() == '':
        gols = '0'
    print(f'O jogador {jogador} fez fez {gols} gols no campeonato')

joga = input('Nome do jogador: ')
gol = input('Gols no campeonato: ')
info(joga, gol)