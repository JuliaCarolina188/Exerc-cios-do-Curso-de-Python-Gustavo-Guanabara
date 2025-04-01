termo = int(input('Digite o primeiro número da progressão: '))
razao = int(input('Digite a razão (diferença) entre os termos: '))
ref = 10
print('A progressão é a seguinte:')
while ref != 0:
    print(f'{termo}', end='')
    print(', ' if ref > 1 else '', end='')
    termo += razao
    ref -= 1