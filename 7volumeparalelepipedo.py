#Declaração de variáveis
altura: float = 0
largura: float = 0
profundidade: float = 0
volume: float = 0

#início
altura = float(input('Digite a altura do paralelepípedo:'))
largura = float(input('Digite a largura do paralelepípedo:'))
profundidade = float(input('Digite a profundidade do paralelepípedo:'))
volume = altura * largura * profundidade
print('O volume do paralelepípedo é:', volume)
