termo = int(input('Digite o primeiro número da progressão: '))
razao = int(input('Digite a razão (diferença) entre os termos: '))
print('A progressão é a seguinte:')
for c in range(termo, termo + (razao * 10), razao):
    print(c)