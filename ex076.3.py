produtos  = 'Pao', '1', 'Bolo', '5', 'Antílope', '100','Pãodequejio', '3', 'Marco', '0'
print(f'{'Produto':-^15}{'Preço':-^15}')
for i in produtos:
    if i.isalpha():
        print(f'{i:^15}', end='')
    elif i.isnumeric():
        print(f'{i:^15}')