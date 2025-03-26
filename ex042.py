n1 = maior = menor = int(input('Digite a primeira reta: '))
n2 = int(input('Digite a segunda reta: '))
n3 = int(input('Digite a terceira reta: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n3 + n2 > n1:
    print('É possível formar um triângulo com essas retas!')
    if n1 == n2 == n3:
        print('Não só isso, mas ele também é um triângulo equilátero, que tem todos os lado iguais')
    elif n1 == n2 or n1 == n3 or n2 ==  n3:
        print('Não só isso, mas ele também é um triângulo isósceles, que tem dois lados iguais')
    elif n1 != n2 and n2 != n3:
        print('Não só isso, mas ele também é um triângulo escaleno, que tem todos os lados diferentes')
else:
    print('Não é possível formar um triângulo com essas retas')