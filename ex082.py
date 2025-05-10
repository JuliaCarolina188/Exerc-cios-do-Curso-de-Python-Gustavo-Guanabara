lista = []
print('Digite vários números. Para parar, só digitar uma letra')
while True:
    n = input('>')
    if n.isalpha():
        break
    else:
        lista.append(int(n))
lista_par = []
lista_impar = []
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)
    else:
        lista_impar.append(i)
print('Lista digitada: ')
print(lista)
print('Números pares: ')
print(sorted(lista_par))
print('Números ímpares: ')
print(sorted(lista_impar))