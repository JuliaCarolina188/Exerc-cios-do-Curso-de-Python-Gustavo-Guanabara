n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

m = (n1 + n2)/2
print(f'Sua média foi de {m}')

if m < 5:
    print('Você está reprovado')
elif 5 <= m <= 6.9:
    print('Você está em recuperação')
elif m > 6.9:
    print('Você foi aprovado')