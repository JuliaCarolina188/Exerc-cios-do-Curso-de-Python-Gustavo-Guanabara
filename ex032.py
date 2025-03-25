ano = int(input('Digite um ano qualquer: '))
print(f'O ano \033[34m{ano}\033[m é bissexto' if ano % 4 == 0 else f'O ano \033[35m{ano}\033[0m não é bissexto')