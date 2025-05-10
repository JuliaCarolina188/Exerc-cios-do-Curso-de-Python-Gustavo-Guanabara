from random import randint
nums = randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)
print('Os números sorteados foram: ', end='')
ref = 1
for c in nums:
    if ref == 5:
        print(f'{c}.')
        break
    print(f'{c}, ', end='')
    ref += 1

ordenada = sorted(nums)
print(f"Menor número: {min(nums)} \nMaior número: {max(nums)}")
print(f'Os números em ordem crescente ficam: ', end='')
ref = 1
for c in ordenada:
    if ref == 5:
        print(f'{c}.')
        break
    print(f'{c}, ', end='')
    ref += 1