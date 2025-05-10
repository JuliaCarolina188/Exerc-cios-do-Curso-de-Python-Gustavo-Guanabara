print('Por favor, digite 5 valores numéricos:')
valores = [int(input('>')), int(input('>')), int(input('>')), int(input('>')), int(input('>'))]

print(f'''O maior valor digitado foi {max(valores)}, na posição {valores.index(max(valores))+1}
O menor valor digitado foi {min(valores)}, na posição {valores.index(min(valores))+1}''')