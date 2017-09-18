#========================================
#=============== lfontesc ===============
#========================================

# Operadores Relacionais na pratica

numero1 = input("Digite um numero")
numero1 = int(numero1)

numero2 = input("Digite um segundo numero")
numero2 = int(numero2)

if (numero1 == numero2):
    print("O numero %d é igual a %d." %(numero1,numero2))
if (numero1 != numero2):
    print("O numero %d é diferente de %d." % (numero1, numero2))
if (numero1<numero2):
    print("O numero %d é menor que o %d." % (numero1, numero2))
if (numero1 > numero2):
    print("O numero %d é maior que o %d." % (numero1, numero2))
if (numero1>=numero2):
    print("O numero %d é maior ou igual a %d." % (numero1, numero2))
if (numero1<=numero2):
    print("O numero %d é menor ou igual a %d." % (numero1, numero2))

