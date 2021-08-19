A = float(input('Digite sua primeira nota:'))
B = float(input('Digite sua segunda nota:'))
S1 = A + B
S2 = S1 / 2
print('Sua média é {}'.format(S2))
if S2 > 6:
    print('parábens você passou de ano!')
else:
    print('Lamento, Você não passou de ano, Se esforce mais!')
