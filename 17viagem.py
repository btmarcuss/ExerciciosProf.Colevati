#declaração de variaveis
litros: float = 0.0
velocidademedia: float = 0.0
gastodegasolina: int = 0
percurso: int = 0
tempopercurso: float = 0.0

#inicio
tempopercurso = int(input("digite quanto tempo durará a viagem:"))
velocidademedia = float(input("digite a velocidade media usada no percuso:"))
gastodegasolina = 12
percurso = (tempopercurso * velocidademedia)
litros = (percurso /gastodegasolina)
print (f"serão gastos {litros} litros nessa viagem.")
#fim