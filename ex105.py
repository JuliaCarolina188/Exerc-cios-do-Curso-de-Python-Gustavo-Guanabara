def notas():
    notas = []
    info = {}
    print('Digite sua sequência de notas: ')
    while True:
        a = input('>')
        while not a.isnumeric():
            a = input('   Isso não foi um número. >')
        while True:
            if 0 <= float(a) <= 10:
                break
            a = input('   Esse número não é aceito. >')
        notas.append(float(a))
        r = input('   Deseja continuar(s/n)? ').lower()
        while r not in 'sn':
            r = input('   Deseja continuar(s/n)? ').lower()
        if r in 'n':
            break
    info['maior nota'] = max(notas)
    info['menor nota'] = min(notas)
    info['media da turma'] = sum(notas) / len(notas)
    return info

boletim = notas()
print(boletim)