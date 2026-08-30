#declaração de variaveis
angulo1: int = 0
angulo2: int = 0
angulo3: int = 0
angulototal: int = 0

#inicio
angulo1 = int(input("digite o primeiro angulo:"))
angulo2 = int(input("digite o segundo angulo:"))
angulo3 = 180 - (angulo1 + angulo2)
if(angulo1 < 0):
    print("angulo invalido")
elif(angulo2 < 0):
    print ("angulo invalido")
elif(angulo1 + angulo2 + angulo3 > 180):
    print ("angulos invalidos")
elif(angulo3 < 0):
    print("angulo invalido")
else:
    print (f"o valor do terceiro angulo é {angulo3} ")