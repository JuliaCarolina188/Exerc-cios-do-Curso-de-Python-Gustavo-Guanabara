matriz = []
print('''1   2   3
4   5   6
7   8   9''')
print('Preencha a seguinte matriz: ')
for i in range(1, 10):
    matriz.append(int(input(f'{i}>')))
print(f'''{matriz[0]}   {matriz[1]}   {matriz[2]}
{matriz[3]}   {matriz[4]}   {matriz[5]}
{matriz[6]}   {matriz[7]}   {matriz[8]}''')