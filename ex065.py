count = som = 0

print('Digite um número: ')
i = men = mai = int(input('>'))
mais = input('Você quer continuar digitando(s/n)? ').lower()

while mais != 'n':
    i = int(input('>'))
    count += 1
    som += i
    if i > mai:
        mai = i
    if i < men:
        men = i
    mais = input('Você quer continuar digitando números(s/n)? ').lower()

print(f'''A média entre os números digitados é de {som / count:.2f}
O maior foi {mai} e o menor foi {men}''')