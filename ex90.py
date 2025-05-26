dic = {'Nome':input('Digite o nome do aluno: '), 'media':float(input('Digite a média desse aluno: '))}
if dic['media'] <= 4:
	dic['Situacao'] = 'reprovado'
elif 5 <= dic['media'] <= 6:
	dic['Situacao'] = 'recuperação'
elif dic['media'] > 6:
	dic['Situacao'] = 'aprovado'

for key, value in dic.items():
	print(f'{key} é {value}')