# Tuplas
#A tupla tem o mesmo comportamento que o Array mas a diferença é que a tupla é imutável, não aceita modificações
tuplaCarros = ("HRV", "Golf", "Argo")
#Converter uma tupla para um array e adicionar os valores
listaCarros = list(tuplaCarros)
listaCarros[2] = "Focus"
tuplaCarros = tuple(listaCarros)
for x in tuplaCarros:
    print(x)