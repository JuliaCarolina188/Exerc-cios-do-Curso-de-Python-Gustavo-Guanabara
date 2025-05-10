produtos  = 'Pao', 0.33, 'Bolo', 5, 'Antílope', 100,'Pão de queijo', 3, 'Marco', 'Imensurável'
print(f'\033[35m{'Produto':_<15}{'Preço':_>15}\033[0m')
for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:_<15}', end='')
    else:
        print(f'{produtos[i]:_>15}')