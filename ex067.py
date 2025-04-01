from time import sleep
while True:
    n = int(input('Digite um número para receber sua tabuada: '))
    if n < 0:
        break
    for i in range(0, 11):
        print(f'{n} x {i} = {n*i}')
        sleep(0.3)
print('fim do processo')