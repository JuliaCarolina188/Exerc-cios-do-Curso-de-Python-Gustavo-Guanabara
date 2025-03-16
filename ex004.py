valor = input('Digite algo: ')
print('O tipo de dado é', type(valor))
print(f'''É alfabético? {valor.isalpha()}
É numérico? {valor.isnumeric()}
É alfanumérico? {valor.isalnum()}
É nulo? {valor.isspace()}
É escrito totalmente em maiúsculo? {valor.isupper()}
É escrito totalmente em minúsculo? {valor.islower()}''')