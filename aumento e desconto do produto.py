A = float(input('Qual é o valor deste produto? R$'))
S = A - (A * 15 / 100)
D = A + (A * 8 / 100)
print('À vista o produto tem 15% de desconto. \nParcelado terá 8% no aumento do preço.')
print('O valor com desconto irá ser de R${:.2f} e com o aumento irá ser de R${:.2f}.'.format(S, D))

B = float(input('Qual opção do senhor? 0 para (À vista) e 1 para (Parcelado):'))

if B < 1:
    print('O senhor optou pela opção à vista!, O Valor pago será de R${:.2f}.'.format(S))
else:
    print('O senhor optou pela opção parcelada!, O valor pago será de R${:.2f}'.format(D))
