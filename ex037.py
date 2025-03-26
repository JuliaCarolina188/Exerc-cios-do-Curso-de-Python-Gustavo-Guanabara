c = int(input('Digite o número inteiro: '))
a = input('''Agora digite para qual base você quer converter:
1 - binário
2 - octal
3 - hexadecimal
>''')

if a == '1':
    print(f'O número {c} em binário é igual a {bin(c)[2:]}')
elif a == '2':
    print(f'O número {c} convertido para octal é igual a {oct(c)[2:]}')
elif a == '3':
    print(f'O número {c} convertido para hexadecimal é igual a {hex(c)[2:]}')
else:
    print('Não foi possível identificar o que você quer fazer')