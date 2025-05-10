lista = []
total = 0
print('Digite uma série de números. Para parar, escreva uma letra.')
while True:
    n = input('>')
    if n.isalpha():
        break
    else:
        lista.append(int(n))
        total += 1
print(f'Você digitou {total} números')
print(f'A lista de valores em ordem decrescente é: ', end='')
invertida = sorted(lista, reverse=True)
for i in range(0, len(lista)):
    if i == len(lista) - 1:
        print(f'{invertida[i]}. ')
    else:
        print(f'{invertida[i]}, ', end='')
if 5 in lista:
    print(f'O número 5 apareceu na posição {lista.index(5)+1}')
else:
    print('O número 5 não aparece')