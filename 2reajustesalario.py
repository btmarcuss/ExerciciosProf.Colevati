#declaracao de variaveis
salario: float = 0.0
reajuste: float = 0.0
salariofinal: float = 0.0

#inicio
reajuste = float(input("digite a porcentagem do reajuste sem o simbolo:"))
reajuste = float(reajuste * 0.01)
salario = float(input("digite o valor do salario"))
salariofinal = (salario + (salario*reajuste))
print (salariofinal)
#fim
