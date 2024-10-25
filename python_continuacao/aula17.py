#Dictionary
#É uma coleção aberta para trabalhar com indexação, mudanças, adicionar e retirar
import os
os.system("cls")

#Sempre na ordem de chave e depois valor
carro = {"Fabricante" : "Honda",
          "Modelo" : "HRV", 
          "Ano" : "2016", 
          "Cor" : "Prata"
}

print(carro["Fabricante"])

#ou

fab = carro.get("Fabricante") #Retorna o valor selecionado dentro do dicionário
fab = carro("Fabricante") #Retorna o valor selecionado dentro do dicionário

#Para mudar as variáveis
carro["cor"] = "Preto"

#Percorrer loop para percorrer as chaves

for x in carro:
    print(x)

#Percorrer loop para percorrer os valores

for x in carro:
    print(carro[x])

#Imprimir itens

for chave, valor in carro.items():
    print(chave + ": " + valor)

#Como verificar se tem itens

if "Modelo" in carro:
    print("Sim, modelo é uma chave")

#Descobrir o tamanho do dictionary (É quantos itens tem, e não quantas palavras)
print("Tamanho do dictionary" + str(len(carro)))

#Adicionar itens em um dictionary

carro["Cambio"] = "Automático"

#Remover itens em um dictionary

carro.pop("Cambio")
#ou
del carro ["Cambio"]
#ou limpar tudo
carro.clear

#------------------------------------------------------------

carros = {
    "Carro1": {
        "Fabricante": "Honda",
        "Modelo": "HRV"
    },
    "Carro2": {
        "Fabricante": "Toyota",
        "Modelo": "Corolla"
    },
    "Carro3":{
        "Fabricante": "Wolksvagen",
        "Modelo": "Up"
    }
}

#Imprimir as variáveis presentes no Dictionary

print(carros["Carro1"])

#imprimir informações específicas
print(carros["Carro1"], ["Fabricante"])

#É possível criar um dictionary para cada item e criar um para todos


Carro1 = {
    "Fabricante": "Honda",
    "Modelo": "HRV"
}
Carro2 = {
    "Fabricante": "Toyota",
    "Modelo": "Corolla"
}
Carro3 = {
    "Fabricante": "Wolksvagen",
    "Modelo": "Up"
}

Carros = {      
    "C1" : Carro1,
    "C2" : Carro2,
    "C3" : Carro3,
}
    