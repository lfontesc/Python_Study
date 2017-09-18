#========================================
#=============== lfontesc ===============
#========================================

# Bloco de Instrução na Pratica

numero = int(input("Digite um Numero: "))

if(numero > 10):
    print("valor é maior que 10!")
    if(numero<= 15):
        print("o valor é maior do que 10 mas menor do que 15")
    else:
        if(numero<=50):
            print("O valor é maior do que 10, mas menor do que 50")
        else:
            print("o valor é maior do que 50")
else:
    if(numero>5):
        print("O Numero é menor que 10 e maior que 5")
        if(numero==7):
            print("O numero é 7")
    else:
        print("O valor é menor que 5")