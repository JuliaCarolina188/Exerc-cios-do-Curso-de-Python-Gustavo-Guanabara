from time import sleep
def maior(* num):
    maior = 0
    sleep(0.5)
    print('Analisando os valores...')
    for i in num:
        print(f'{i} ', end='')
        sleep(0.5)

        if i > maior:
            maior = i
    sleep(1)
    print(f'\nForam analisados {len(num)} números ao todo. O maior número dessa lista é o {maior}')

maior(0, 4, 6, 2, 7, 8, 3, 6)
maior(4, 7, 0)
maior(1, 2)
maior()