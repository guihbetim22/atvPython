with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
print("Teste do arquivo inicial", type(conteudo))
print("\nConteudo do arquivo:",conteudo)
