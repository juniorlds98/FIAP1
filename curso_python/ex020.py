import random

alunos = ["Junior", "Bruno", "Carmine", "Thiago"]

print ("Sorteio da apresentação")
print("")
print(f"A ordem para apresentação será: {random.sample(alunos, k = 4)}")