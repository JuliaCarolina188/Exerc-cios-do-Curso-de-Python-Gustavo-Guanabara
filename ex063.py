ref = int(input('Digite quantos termos você uqer ver da sequência: '))
argumento_1 = 1
argumento_2 = 0
print(f"\033[35m{argumento_2}\033[0m, {argumento_1}", end='')
while ref-1 != 0:
    resultado = argumento_2 + argumento_1
    print(f', {resultado}', end='')
    argumento_2 = argumento_1
    argumento_1 = resultado
    ref -= 1