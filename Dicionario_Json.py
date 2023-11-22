import json

diconario = {
  "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
  "Quico":["Quico Flores","24/04/2017","Raiox_01"],
  "Quico":["Florinda Flores","18/04/2017","Recep_03"]
}

with open("bd1.json", "w") as json_file:
    json.dump(diconario, json_file)