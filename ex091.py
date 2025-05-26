from random import randint
from operator import itemgetter
dic = dict()
for i in range(1, 5):
    dic[f'Jogador {i}'] = randint(1, 6)
for key, value in dic.items():
    print(f'O {key} sorteou {value}')
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
print(f'{'Ranking':-^28}')
for i in range(0, len(ranking)):
    print(f'{i+1}º lugar: {ranking[i][0]}, com {ranking[i][1]}')