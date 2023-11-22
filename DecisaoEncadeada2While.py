nome=input("Digite o nome: ")
idade=int(input("DIgite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
genero=input("Digite o gênero do paciente: ").upper()
gravidez=input("A paciente está gravida? ").upper()

# PRIMEIRO ORIBLEMA A SER RESOLVIDO
while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!="NAO":
    print("Digite SIM ou NAO")

if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
else:
    print("Encaminhe o paciente para sala BRANCA")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM Prioridade")
else:
    if genero=="FEMININO" and idade>10:
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
