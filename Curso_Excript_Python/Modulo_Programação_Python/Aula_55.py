#========================================
#=============== lfontesc ===============
#========================================

# EXEMPLO COM OPERADOR IN

# a = 10
# b = 25
# c = 66
#
# x = int(input("Digite um numero: "))
# #if (x == a or x == b or x == c ):
# if(x in[a,b,c]):
#     print("Sim.")
# else:
#     print("Não.")

#---------------------------------------
cores = ["azul","amarelo","vermelho","branco"]

while True:
    valor = input("Digite o nome de uma cor ou 0 para sair do programa: \n")
    if (valor == "0"):
        break
    elif valor in cores:
        print("Esta na lista de cores xD;\n")
    else:
        print("Nao esta na lista de cores :/;\n")