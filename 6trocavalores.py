#declaração de variáveis
X: float = 0
Y: float = 0
C: float = 0

#início
X = float(input('digite o valor de X:'))
Y = float(input('digite o valor de Y:'))
C = X
X = Y
Y = C
print('O valor de X é:', X)
print('O valor de Y é:', Y)
