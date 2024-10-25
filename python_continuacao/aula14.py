#loop while
# O loop tradicional serve para realizar um bloco de comandos

#inicialização de variável de controle
#while (teste lógico)
    #comando1
    #comando2
    #comandoX
    #incremento ou decremento ou controle da variável
    #Tomar cuidado com o incremento ou o decremento da variável
    #Em algum momento ele tem que devolver o resultado False, se não ele entra em loop infinito

import os
os.system("cls") #limpar a tela


i = 0
carros = ["HRV", "Golf", "Argo", "Onix", "Focus"]
tamanho = len(carros)

while i<tamanho:
    print(carros[i])
    i += 1
print("Fim do loop")

while i < 10:
    print(i)
    i += 1
    if(i>=5):
        break
print("Fim do loop")

#------------------------------------------------------------#

carro = input("Digite o nome do novo carro: ")
carros = []
tamanho = len(carros)

while carro != "-1":
    carros.append(carro)
    carro = input("Digite o nome do novo carro: ")

os.system("cls")
for x in carros:
    print(x) 

print("Fim do loop")
