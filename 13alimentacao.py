#declaração de variaveis
alimentoskg: float = 0.0
consumo: float = 0.0
pessoas: int = 0
duracaodealimentos: float = 0.0

#inicio
alimentoskg = float(input("digite a quantidade de kilos de alimento:"))
consumo = 0.05
pessoas = int(input("digite a quantidade de pessoas:"))
duracaodealimentos = alimentoskg/(pessoas * consumo)
if (duracaodealimentos<1):
    print("A comida durará por menos de um dia.")
else:
    print (f"A comida durará {duracaodealimentos:.2f} dias.")