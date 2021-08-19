A = float(input('Qual a Largura da parede?'))
B = float(input('Qual a altura da parede?'))
S = A * B
D = S / 2
print('Sua parede tem uma dimensão de {}X{} e sua área é de {}M². \nPara pinta sua parede, você precisará de {}l de tinta.'.format(A,B, S, D))