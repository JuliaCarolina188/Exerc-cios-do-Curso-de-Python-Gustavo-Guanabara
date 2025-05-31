import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except:
    print('O site pudim não está acessível no momento')
else:
    print('Tudo ok')
    print(site.read())