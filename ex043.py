peso = float(input('Digite o seu peso, em kg: '))
altura = float(input('Digite a sua altura, em metros: '))

cores = {'roxo':'\033[35m', 'limpo':'\033[0m'}

imc = peso / altura**2

print(f'O seu {cores['roxo']}imc{cores['limpo']} é de {cores['roxo']}{imc:.2f}%{cores['limpo']} que é considerado {cores['roxo']}', end = '')
if imc <=18.5:
    print('abaixo do peso')
elif imc <= 25:
    print('o peso ideal')
elif imc <= 30:
    print('sobrepeso')
elif imc <= 40:
    print('obesidade')
elif imc > 40:
    print('obesidade mórbida')