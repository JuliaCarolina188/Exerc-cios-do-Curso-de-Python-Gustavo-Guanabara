nums = [[], []]
print('Digite 7 valores: ')
for i in range(0, 7):
    n = int (input('>'))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
nums[0].sort()
nums[1].sort()
print(f'No fim, você digitou {len(nums[0])} números pares: ')
for i in range(0, len(nums[0])):
    if i == len(nums[0]) - 1:
        print(f'{nums[0][i]}.')
    else:
        print(f'{nums[0][i]}, ', end='')
print()
print(f'E {len(nums[1])} números impares: ')
for i in range(0, len(nums[1])):
    if i == len(nums[1]) - 1:
        print(f'{nums[1][i]}.')
    else:
        print(f'{nums[1][i]}, ', end='')