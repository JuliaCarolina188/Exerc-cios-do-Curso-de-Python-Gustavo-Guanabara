from datetime import date
def voto(ano):
    idade = date.today().year - ano
    print(f'Com {idade} anos, voto ', end='')
    if idade < 16:
        return f'NEGADO'
    elif 18 > idade >= 16 or idade >= 75:
        return F'OPCIONAL'
    else:
        return f'OBRIGATÓRIO'

vot = voto(int(input('Digite o seu ano de nascimento: ')))
print(vot)