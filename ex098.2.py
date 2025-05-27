from time import sleep
def fors(inicio, fim, passo):
    print('=-'*30)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont < fim+1:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.5)
        print('FIM')
        sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.5)
        print('FIM')
        sleep(0.5)


fors(1, 10, 1)
fors(10, 0, 2)
ini = int(input('Digite o número de início: '))
fi = int(input('Digite o último número: '))
pas = int(input('Digite quantos números serão pulados: '))
fors(ini, fi, pas)