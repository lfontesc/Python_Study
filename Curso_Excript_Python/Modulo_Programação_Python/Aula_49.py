#========================================
#=============== lfontesc ===============
#========================================

# incluir , alterar , excluir lista

lista = [2,3,4]
print(lista)
lista.append(5)
print(lista)
lista.insert(0,2)
print(lista)
lista[1] = 10
print(lista)
lista.clear()
print(lista)
lista = [2,2,2,3]
lista.pop()
print(lista)
lista.append(4)
print(lista)
del(lista[0:2])
print(lista)