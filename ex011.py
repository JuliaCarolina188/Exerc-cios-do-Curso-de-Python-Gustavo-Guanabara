altura = int(input('Digite qual é a altura da parede que quer pintar: '))
largura = int(input('Digite qual é a largura da parede que quer pintar: '))

print(f'''Sabendo que a área total é {largura*altura},
e que cada litro de tinta pinta 2m quadrados, você precisará de {(largura*altura)/2}''')