import random #ou pode so importa o (Choice). from random import choice
print('Uma professora precisa da ajuda de um aluno para apagar o quadro, ajude-a a sortear um aluno.')
n1 = str(input('Primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('Terceiro nome:'))
n4 = str(input('quarto nome:'))
n5 = str(input('Quinto nome:'))
lista = [n1, n2, n3, n4, n5]  # Se usa [] quando for criar uma lista
escolhido = random.choice(lista)

print('\nO aluno escolhida foi {}'.format(escolhido))