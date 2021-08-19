A = float(input('Qual o seu salário? R$'))
#S = A * 15 / 100
#D = A + S
S = A + (A * 15 / 100)
print('Você recebe R${:.2f}, com um aumento de 15% você ira receber R${:.2f}'.format(A, S))