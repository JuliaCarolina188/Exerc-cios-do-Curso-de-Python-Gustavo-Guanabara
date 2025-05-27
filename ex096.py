def area(comprimento, largura):
    print(f'A área de um terreno de {comprimento} x {largura} é de {comprimento*largura} metros quadrados')

print('Controle de terrenos')
print('-'*20)
com = float(input('Comprimento(m): '))
lar = float(input('Largura(m): '))
area(com, lar)