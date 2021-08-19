A = int(input('Quantos dias alugados?'))
B = float(input('Quantos Km rodados?'))
S = (A * 60) + (B * 0.15)
print('O aluguel do carro vai ficar no valor de R${:.2f}'.format(S))
