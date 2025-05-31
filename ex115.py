from time import sleep
from ex115_Modulos import *
from ex115_Arquivo import *
pessoas = []
temp = {}

arq = 'cursoemvideo.txt'
if arquivo_existe(arq):
    print('Arquivo encontrado')
else:
    print('Arquivo não encontrado')
    criar_arquivo(arq)

while True:
    titulo('MENU PRINCIPAL')
    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Parar o programa'])
    op = validador_de_op()
    if op == 1:
        ler_arquivo(arq)
        '''titulo('Ver pessoas cadastradas')
        for indice, pessoa in enumerate(pessoas):
            print(f'ID: {indice}')
            for key, value in pessoa.items():
                print(f'   {key}: {value}')'''
    elif op == 2:
        titulo('Cadastrar uma nova pessoa')

        nome = input('Nome: ')
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)

    elif op == 3:
        titulo('Sair do programa')
        break