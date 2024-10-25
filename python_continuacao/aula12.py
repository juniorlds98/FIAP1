# loop for

carros = ["HRV", "Golf", "Argo", "Focus", "Fit", "Fusion", "Polo"]

#Para percorrer a coleção inteira eu crio uma variável para receber os itens da coleção (x)
#E com o in eu sinalizo qual coleção eu quero percorrer
#Se precisar percorrer uma lista é só eu usar o for x in
for x in carros:
    print(x)
    if(x==carros):
        print("  VW")
#É possível percorrer os elementos de itens como variáveis, listas ou até strings
for x in "CFB Cursos":
    print(x)
#É possível usar o movimento break para encontrar um item específico e parar ali
for x in carros:
    if(x == "Fit"):
        break
    print(x)

print("Fim do programa")