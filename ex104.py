def leiaint():
    n = input('>')
    while not n.isnumeric():
        n = input('Isso não é um número. \n   Digite um número:')
    return int(n)

c = leiaint()
print(f'Você acabou de digitar o número {c}')