# Matrizes É uma coleção de array
import os
os.system("cls")

carros = [
    ["Modelo", "HRV"], # 0 0
    ["Fabricante","Honda"], # 1 1
    ["Ano","2016"] # 2 2
] 

carros.append(["Cor", "Prata"]) #Inserção de informação
#ou
carros.insert(["Cambio","Automatico"]) #Inserção de informação

carros [1][1] = "Hondinha" #Trocar valor

print(carros [0][0]) #Printar valores

print(carros[1][1])

for linha, coluna in carros:
    print("Linha: " + linha + " | Coluna: " + coluna + "\n")