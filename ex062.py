from traceback import print_tb

termo = int(input('Digite o primeiro número da progressão: '))
razao = int(input('Digite a razão (diferença) entre os termos: '))
ref = mais_termos = 10
termos_mostrados = 0
print('A progressão é a seguinte:')
while mais_termos != 0:
    ref = mais_termos
    while ref != 0:
        print(f'{termo}', end='')
        print(', ' if ref > 1 else '', end='')
        termo += razao
        ref -= 1
        termos_mostrados += 1
    mais_termos = int(input("\nDigite quantos termos mais você quer ver: "))
print(f'Fim da execução. {termos_mostrados} termos foram mostrados')