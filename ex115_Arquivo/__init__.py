from ex115_Modulos import titulo
def arquivo_existe(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(',')
            print(f'{dado[0]:_<20}{dado[1]:_>20}')
    finally:
        a.close()

def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome},{idade} \n')
        except:
            print('Houve algum erro ao tentar escrever no arquivo')
        else:
            print('Informações adicionadas no arquivo')
            a.close()