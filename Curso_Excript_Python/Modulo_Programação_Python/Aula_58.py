#========================================
#=============== lfontesc ===============
#========================================

# Propriedade das Strings
from builtins import str

s = "Lista de Caracteres"
print(len(s))
lista = s.split(" ")
lista = lista[0] +" "+ lista[2]
print(lista)

print(s.replace("de", ""))