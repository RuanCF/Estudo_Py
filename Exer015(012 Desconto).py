A = float(input('Qual o preço do produto? R$'))
S = A * 10 / 100
D = A - S
print('O produto no valor de R${}. está na promoção com 10% de desconto, O produto irá ficar no valor de R${}'.format(A, D))