valores = []
mai = min = 0
print('Digite 5 valores: ')
for i in range(0, 5):
    valores.append(int(input('>')))
    if i == 0:
        min = valores[i]
    if valores[i] > mai:
        mai = valores[i]
    if valores[i] < min:
        min = valores[i]

print(f'''Maior valor: {mai}, na posição {valores.index(mai)+1}
Menor valor: {min}, na posição {valores.index(min)+1}''')