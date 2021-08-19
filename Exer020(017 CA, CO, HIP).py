import math
''' CO = float(input('Cateto oposto' ))
CA = float(input('Cateto adjacente' ))
HI = (CO ** 2 + CA ** 2) ** (1/2)
print('A Hipotenusa é: {:.2f}'.format(HI)) '''

CO = float(input('Cateto oposto'))
CA = float(input('Cateto adjacente'))
HI = math.hypot(CA, CO)
print('A Hipotenusa é: {:.2f}'.format(HI))