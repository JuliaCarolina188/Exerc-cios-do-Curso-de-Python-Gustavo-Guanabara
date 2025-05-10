nums = []
print('Digite uma série de números')
while True:
    n = int(input('>'))
    if n in nums:
        print('Número repetido. Deseja continuar? ')
        r = input('(s/n)>').lower()
        if 'n' in r:
            break
        while 's' not in r:
            r = input('(s/n)>').lower()
    else:
        nums.append(n)

print('A lista final ficou: ')
for i in range(len(nums)):
    if i == len(nums)-1:
        print(f'{nums[i]}.')
    else:
        print(f'{nums[i]}, ', end='')