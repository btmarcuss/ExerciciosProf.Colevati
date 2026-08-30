import math
#declaracao de variaves
A: float = 0
B: float = 0
C: float = 0
D: float = 0
X1: float = 0
X2: float = 0

#inici0
A = float(input('digite o valor de A:'))
B = float(input('digite o valor de B:'))
C = float(input('digite o valor de C:'))


if (A == 0):
    print('coeficiente igual a 0')
else:
    D = ((B**2)-(4*A*C))
    if (D < 0):
        print('Nao possui raiz real')
    elif (D == 0):
        X1 = ((-B + math.sqrt(D))/(2 * A))
        print(X1)
    else:
       X1 = (-B + math.sqrt(D))/(2*A)
       X2 = (-B - math.sqrt(D))/(2*A)
       print(X1)
       print(X2)
