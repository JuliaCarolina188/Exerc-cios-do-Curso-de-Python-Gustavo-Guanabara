km = int(input('Digite quantos quilômetros sua viajem terá: '))
print(f'Sua viajem custará {km * 0.5:.2f}R$' if km <= 200 else print(f'Sua viagem custará {km*0.45:.2f}R$'))