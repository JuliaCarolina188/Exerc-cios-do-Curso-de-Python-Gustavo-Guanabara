matriz = [[], [], []]
print('''
    1   2   3
1   x   x   x
2   x   x   x
3   x   x   x''')
print('Preencha a seguinte matriz: ')
for i in range(0, 3):
    matriz[0].append(int(input(f'1, {i}>')))
for i in range(0, 3):
    matriz[1].append(int(input(f'2, {i}>')))
for i in range(0, 3):
    matriz[2].append(int(input(f'3, {i}>')))

print(f'''{matriz[0][0]}   {matriz[0][1]}   {matriz[0][2]}
{matriz[1][0]}   {matriz[1][1]}   {matriz[0][2]}
{matriz[2][0]}   {matriz[2][1]}   {matriz[2][2]}''')