usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Quico Flores","24/04/2017","Raiox_01"],
    "Quico":["Florinda Flores","18/04/2017","Recep_03"]
}

usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("#########=====#####")
print("Dados: ",usuarios.get("Chaves"))