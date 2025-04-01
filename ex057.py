sex = input('Digite qual é seu sexo(m/f): ').upper().strip()[0]
while sex not in 'MmFf':
    sex = input('Digite qual é seu sexo(m/f): ').upper().strip()[0]
print('Obrigada por responder a pesquisa')