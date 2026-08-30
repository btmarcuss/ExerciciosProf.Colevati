#declaração de variaveis
anonascimento: int = 0
anoatual: int = 0
idadeatual: int = 0
idadeem17: int = 0

#inicio
anonascimento = int(input("digite o ano de nascimento:"))
anoatual = int(input("digite o ano atual:"))
idadeatual = (anoatual - anonascimento)
idadeem17 = (idadeatual + 17)
if (idadeatual<0):
    print ("idade invalida")
else:
    print (f"sua idade atual é {idadeatual}, e em 17 anos você terá {idadeem17}!")
