produtos  = 'Pao', 0.33, 'Bolo', 5, 'Antílope', 100,'Pão de queijo', 3, 'Marco', 'Imensurável'
print(f'{'Produto':-^15}{'Preço':-^15}')
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:^15}{produtos[i+1]:^15}')