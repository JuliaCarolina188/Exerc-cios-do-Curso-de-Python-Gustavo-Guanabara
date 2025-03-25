n1 = maior = menor = int(input('Digite a primeira reta: '))
n2 = int(input('Digite a segunda reta: '))
if n2 > n1:
    maior = n2
if n2 < n1:
    menor = n2
n3 = int(input('Digite a terceira reta: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
medio = maior
#Medio
if menor < n1 < maior:
    medio = n1
if menor < n2 < maior:
    medio = n2
if menor < n3 < maior:
    medio = n3
print(f'O maior lado mede: \033[35m{maior}cm\033[0m. O lado mediano mede: \033[36m{medio}cm\033[0m, e o menor lado mede: \033[32m{menor}cm\033[0m')
print('Essas retas podem formar um triângulo!!' if menor + medio > maior else 'Não é possível formar um triângulo')