while True:
    nums = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
    x = int(input('Digite um número entre 0 e 20: '))
    if 0 < x <= 20:
        break
    print('Tente novamente')
print(f'Você digitou o número \033[35m{nums[x]}')