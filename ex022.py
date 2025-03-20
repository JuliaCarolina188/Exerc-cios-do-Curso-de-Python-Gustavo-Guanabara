n = input('Digite o seu nome: ')
n2 = n.split()

print(f'''Maiúsculas: {n.upper()}
Minúsculas: {n.lower()}
Quantas letras possui: {len(n.replace(' ', ''))}
Primeiro nome: {n2[0]}. Quantas letras tem o primeiro nome: {len(n2[0])}''')