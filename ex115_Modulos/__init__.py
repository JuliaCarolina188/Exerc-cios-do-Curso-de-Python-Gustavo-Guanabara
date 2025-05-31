from time import sleep
def titulo(msg):
    sleep(0.5)
    print('-'*40)
    print(f'{msg:^40}')
    print('-' * 40)
    sleep(0.5)

def menu(lst):
    cont = 1
    for i in lst:
        print(f'{cont} - {i}')
        cont += 1

def validador_de_op():
    while True:
        try:
            r = int(input('Escolha uma opção: '))
        except (TypeError, ValueError):
            print('Opção inválida.')
        except KeyboardInterrupt:
            print('Você decidiu parar o programa. ')
            return 3
        else:
            while True:
                if 0 < r <= 3:
                    break
                try:
                    print('Opção inválida.')
                    r = int(input('Escolha uma opção: '))
                except (TypeError, ValueError, KeyboardInterrupt):
                    continue
            return r

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