import math

angulo = int(input("Escolha um ângulo: "))
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f"O seu ãngulo escolhido foi: {angulo} e ao calcular ele deu os seguintes resultados: \n Seno: {seno} \n Cosseno: {cosseno} \n Tangente: {tangente}")