from time import sleep
frase = input('Digite uma frase: ').replace(' ', '')
letras = frase.split()
tamanho = len(frase)
palas = ''
for i in range(tamanho-1, 0-1, -1):
    print(frase[i], end='')
    palas = palas + frase[i]
    sleep(0.3)
if palas == frase:
    print("\nÉ um palíndromo!")
else:
    print("\nNão é um palíndromo")