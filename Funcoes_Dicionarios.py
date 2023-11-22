lista=[]
dicionario={}

#perguntar as alternativas
def perguntar():
    reposta = input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n"+
                 "<P> - Para Pesquisar um usuário\n"+
                 "<E> - Para Excluir um usuario\n"+
                 "<L> - Para Listar um usuário:\n ").upper()
    return reposta
  
#inserir o usuario  
def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite seu nome: ").upper(),
                         input("Digite a última data de acesso:"),
                         input("Qual a última estacao acessada: ").upper()]
  
#pesquisar o usuario
def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estaçaõ.: " + lista[2])
      
#excluir o usuario
def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")
  
#listar usuarios 
def listar(diconario):
    for chave, valor in dicionario.items():
        print("Objeto.....")
        print("Login: ", chave)
        print("Dados: ", valor)