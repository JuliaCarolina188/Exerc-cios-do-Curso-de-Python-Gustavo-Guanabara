print('Digite o peso de 5 pessoas: ')
maior = menor = input('>')
for i in range(0, 4):
    p = input('>')
    if p > maior:
        maior = p
    if p < menor:
        menor =  p
print(f'''Pessoa mais pesada: {maior}
Pessoa mais leve: {menor}''')