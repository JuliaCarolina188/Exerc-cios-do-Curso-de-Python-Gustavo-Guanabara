from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('''O que você deseja fazer?
[1] somar
[2] multiplicar
[3] mostrar o maior entre eles
[4] informar novos números
[5] sair do programa''')
op = int(input('>'))

while op != 5:
    if op == 1:
        print(f'{n1} + {n2} = {n1+n2}')

    elif op == 2:
        print(f'{n1} x {n2} = {n1*n2}')

    elif op == 3:
        print(f'{n1} é o maior entre os dois' if n1 > n2 else f'{n2} é o maior entre eles')

    elif op == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))

    else:
        print('Opção inválida')

    sleep(3)
    print('-'*20)
    print('''O que mais você deseja fazer?
    [1] somar
    [2] multiplicar
    [3] mostrar o maior entre eles
    [4] informar novos números
    [5] sair do programa''')
    op = int(input('>'))
