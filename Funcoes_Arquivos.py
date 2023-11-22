def chamarMenu(): 
    escolha = int(input("Digite: "
            "\n[1] para registrar um dispositivo:"
            "\n[2] para criar inventario de dados:"
            "\n[3] para exibir items armazenados no inventario: \n"))
    return escolha

def registrar(dicionario):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número de plaqueta patrominial: \n")]=[
        input("Digite a última verificação (data): \n"),
        input("Digite o modelo do item: \n"),
        input("Digite o estado do item: \n")]
        resp=input("Digite <S> para continuar.\n").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + 
                                     valor[1] + ";" + valor[2]+"\n")
    return "Persistindo com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas=inv.readlines()
    return linhas