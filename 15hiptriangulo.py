#declaração de variaveis
cateto1: int = 0
cateto2: int = 0
hipotenusa: int = 0
hipotenusaqua: int = 0

#inicio
cateto1 = int(input("digite o valor do primeiro cateto:"))
cateto2 = int(input("digite o valor do segundo cateto:"))
hipotenusaqua =  (cateto1 **2) + (cateto2 **2)
hipotenusa = (hipotenusaqua ** 0.5)
print (f"a hipotenusa do triangulo é {hipotenusa:.3f}")