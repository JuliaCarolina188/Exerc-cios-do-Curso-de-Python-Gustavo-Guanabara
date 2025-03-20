frase = input('Digite uma frase: ')
ass = frase.lower().count('a')

print(f'''Quantidade de As na frase: {ass}
Caractere onde a letra A apareceu pela primeira vez: {frase.lower().find('a')+1}
Última vez que um A aparece: {frase.lower().rfind('a')+1}''')