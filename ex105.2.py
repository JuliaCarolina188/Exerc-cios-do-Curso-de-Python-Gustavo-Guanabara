def boletim(*notas, situacao=True):
    """Ai q preguiça"""
    info = dict()
    info['maior nota'] = max(notas)
    info['menor nota'] = min(notas)
    info['media da turma'] = sum(notas) / len(notas)
    if (sum(notas) / len(notas)) >= 7:
        info['situação'] = 'BOA'
    elif (sum(notas) / len(notas)) >= 5:
        info['situação'] = 'RAZOÁVEL'
    else:
        info['situação'] = 'RUIM'
    return info

notas_turma = boletim(6, 6, 6)
print(notas_turma)