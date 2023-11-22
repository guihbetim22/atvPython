from Capitulo4_Dicionarios.Funcoes_Dicionarios import *
usuarios={}
opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    opcao = perguntar()
    if opcao=="P":
        pesquisar(usuarios)
    if opcao == "E":
        exluir(usuarios)
    if opcao == "L":
        listar(usuarios)
    opcao= perguntar()
