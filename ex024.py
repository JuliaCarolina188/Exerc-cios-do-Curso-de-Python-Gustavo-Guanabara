n = input('Digite o nome de uma cidade: ')
n2 = n.split()

print(f'O nome da cidade começa com Santo: {'santo' in n2[0].lower()}')