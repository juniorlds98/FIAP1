# Coleção list ou array
carros = ["HRV", "Golf", "Argo", "Focus"]

#Substituição de itens na lista
carros[3] = "Fusion"

#Inclusão de itens na lista
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

#Remover itens da lista
carros.remove("Fusion")

#Remover o último elemento da lista
carros.pop()

#Remover o item pedido
del carros [2]

#limpar a lista inteira
carros.clear()

#copiar a lista
carros2 = list(carros)

#fundir duas listas
carros2 = ["Fusca", "147", "Braslia", "Celta"]
carros3 = carros + carros2

#Descobrir tamanho na lista
print(str(len(carros)) + " Carros na lista")
print(carros)
print(carros2)
print(carros3)




