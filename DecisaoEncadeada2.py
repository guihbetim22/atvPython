nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?").upper()
genero=input("Digite o gênero do paciente: ").upper()
gravidez=input("A paciente está grávida? ").upper()
#abaixo inclui a prioridade de idosos e separando por salas
if idade >= 65:
    print("Paciente COM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Impossivel definir a sala do paciente")
#abaixo define a etapa que inclui o genero, a gravidez da paciente e a idade
else:
    if genero=="FEMININO" and idade>= 10:
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        elif gravidez=="NAO":
            print("Paciente SEM prioridade")
        else:
            print("A paciente esta gravida ? responda com SIM ou NAO")