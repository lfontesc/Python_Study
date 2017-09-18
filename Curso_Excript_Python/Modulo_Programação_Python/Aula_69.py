#========================================
#=============== lfontesc ===============
#========================================

# Retorno de Valores Multiplos

# def func():
#     return 1, 2
# a, b = func()
# print(a,b)
#
# t = (10,20)
# a,b = t

def potencia(x):
    quadrado = x**2
    cubo = x**3
    return quadrado,cubo

q,c = potencia(10)
print(q)
print(c)