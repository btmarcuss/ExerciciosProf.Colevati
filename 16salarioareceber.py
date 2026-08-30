#declaração de variaveis
horastrabalhadas: int = 0
valorhora: float = 0.0
percentualdesconto: float = 0.0
dependentes: int = 0
salariobruto: float = 0.0
salarioliquido: float = 0.0
salariofinal: float = 0.0

#inicio
horastrabalhadas = int(input("digite a quantidade de horas trabalhadas:"))
valorhora = float(input("digite o valor das horas trabalhadas:"))
percentualdesconto = float(input("digite o percentual de descontos sem simbolos:"))
dependentes = int(input("digite a quantidade de dependentes:"))
salariobruto = (horastrabalhadas * valorhora)
percentualdesconto = (percentualdesconto * 0.01)
salarioliquido = (salariobruto - (salariobruto * percentualdesconto))
salariofinal = (salarioliquido + (dependentes * 100))
if (horastrabalhadas < 0):
    print ("horas invalidas")
elif (valorhora < 0):
    print ("valor da hora trabalhada invalido")
elif (percentualdesconto < 0):
    print ("percentual de desconto invalido.")
elif (dependentes < 0):
    print("numero de dependentes invalido.")
else:
    print (f"O salario do trabalhador será {salariofinal}")

