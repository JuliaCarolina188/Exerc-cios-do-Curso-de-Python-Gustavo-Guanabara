n = input('Digite o seu nome completo: ')
n2 = n.split()
print(f'''Primeiro nome: {n2[0]}
Último nome: {n2[len(n2)-1]}''')