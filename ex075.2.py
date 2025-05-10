nums = int(input('Digite um número: ')), int(input('Digite outro: ')), int(input('Mais um: ')), int(input('Último: '))
print(f'Você digitou os valores: {nums}')
print(f'O número 9 apareceu {nums.count(9)} vezes')
if 3 in nums:
    print(f'O valor 3 apareceu pela primeira vez na posição {nums.index(3)+1}')
print(f'O valores pares digitados foram: ')
for i in nums:
    if i % 2 == 0:
        print(f'{i} ', end='')