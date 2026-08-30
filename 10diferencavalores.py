#declaração de variaveis
valor1: int = 0
valor2: int = 0
diferenca: int = 0

#inicio
valor1 = int(input("digite o primeiro valor:"))
valor2 = int(input("digite o segundo valor:"))
if (valor1>valor2):
    diferenca = (valor1 - valor2)
    print (f"o primero valor é maior, então a diferença é {diferenca}")
elif (valor1<valor2):
    diferenca = (valor2 - valor1)
    print (f"o segundo valor é maior, então a diferença é {diferenca}")
else: 
    print ("os valores são iguais")
#fim