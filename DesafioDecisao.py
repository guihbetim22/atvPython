#DEFINIÇÃO DE NIVEL ( ADM, USER, GUEST)

resposta="SIM"
while resposta=="SIM":
    nivel = input("Digite o nivel de acesso: ")
    if nivel=="admin" or nivel=="user":
        genero = input("Digite o seu gênero: ")
        if nivel=="admin":
            if genero=="feminino":
                print("Olá administradora")
            else:
                print("Olá administrador")
        else:
            if genero=="feminino":
                print("Olá usuária")
            else:
                print("Olá usuário")
    elif nivel=="GUEST":
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    resposta = input("Digite SIM para continuar: ").upper()