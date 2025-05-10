print('Digite uma expressão numérica')
ab = fch = []
exp = input('>')
for i in exp:
    if '(' in i:
        ab.append(1)
    elif ')' in i:
        fch.append(1)
if len(ab) != len(fch):
    print('Expressão incorreta')
else:
    print('Expressão correta!')