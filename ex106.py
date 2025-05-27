from time import sleep
def ajuda(msg):
    sleep(1)
    print(help(msg))
    sleep(1)
while True:
    a = input('Função ou biblioteca: ').lower().strip()
    if a == 'fim':
        break
    else:
        ajuda(a)