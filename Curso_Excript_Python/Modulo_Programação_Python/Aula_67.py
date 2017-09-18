#========================================
#=============== lfontesc ===============
#========================================

# Argumentos Nomeados vs Argumentos Posicionais

def dados_pessoais(nome,sobrenome,idade,sexo):
    print("Nome: {}\nSobrenome: {}\nIdade: {}\nSexo: {}".format(nome,sobrenome,idade,sexo))
dados_pessoais("Lucas","Fontes",19,"Masculino")
dados_pessoais(nome="Fontes", sobrenome="Lucas",idade=19,sexo=True)