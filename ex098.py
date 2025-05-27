from time import sleep
def fors(inicio, fim, passo):
    print('=-'*30)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    for i in range(inicio, fim+1, passo):
        print(f'{i} ', end='')
        sleep(0.5)
    print('FIM')
    sleep(0.5)


fors(1, 10, 1)
fors(10, 0, -2)
ini = int(input('Digite o número de início: '))
fi = int(input('Digite o último número: '))
pas = int(input('Digite quantos números serão pulados: '))
fors(ini, fi, pas)