n1 = maior = menor = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n2 > n1:
    maior = n2
if n2 < n1:
    menor = n2
n3 = int(input('Digite o terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
print(f'''O maior número foi \033[36m{maior}\033[0m
e o menor foi \033[36m{menor}\033[0m''')