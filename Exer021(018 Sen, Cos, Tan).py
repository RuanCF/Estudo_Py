import math
A = float(input('Um número:'))
B = math.sin(math.radians(A))
C = math.cos(math.radians(A))
D = math.tan(math.radians(A))
print('O Seno é: {:.2f}\n O Cosseno é: {:.2f}\n A tangente é: {:.2f}'.format(B, C, D))