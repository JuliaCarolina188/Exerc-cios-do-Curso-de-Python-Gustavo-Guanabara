def cabeca(msg):
    tamanho = len(msg) + 6
    print('~'* tamanho)
    print(f'{msg:^{tamanho}}')
    print('~'* tamanho)

cabeca('A')
cabeca('Carolina')
cabeca('Anapurna abcdef aaaa')