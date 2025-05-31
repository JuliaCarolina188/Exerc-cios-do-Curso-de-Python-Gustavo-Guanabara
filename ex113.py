def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mO valor recebido não é um numero válido\033[0m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu não continuar\033[0m')
            return 0
        else:
            return n
def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mO valor recebido não é um numero válido\033[0m')
        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu não continuar\033[0m')
            return 0
        else:
            return n

num = leia_int('Digite um número inteiro: ')
nums = leia_float('Digite um número float: ')
print(f'O numero inteiro digitado foi {num}, e o numero float foi {nums}')