#declaração de variaveis
deposito: float = 0.0
rendimento: float = 0.0
taxa: float = 0.0
meses: int = 0
valorfinal: float = 0.0

#inicio
deposito = float(input("digite o valor que sera depositado na poupança:"))
taxa = float(input("digite a taxa de rendimento mensal:"))
meses = float(input("digite quantos meses o deposito irá render:"))

rendimento = (deposito+(deposito * ((taxa/100)** meses)))
valorfinal = (deposito + rendimento)
print (f"o valor do após {meses} meses será de {valorfinal:.2f}")
#fim