import random
n1 = str(input('Primeiro nome:'))
n2 = str(input('Segundo nome:'))
n3 = str(input('Terceiro nome:'))
lista=[n1, n2, n3]
random.shuffle(lista)
print('A ordem escolhida foi:')
print(lista)