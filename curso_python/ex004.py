algo = input("Escreva algo aqui: ")

print(f"O tipo dela é: {type(algo)}")
print(f"Você escreveu: {algo}")
print(f"Só tem espaços? {algo.isspace()}")
print(f"É númerico? {algo.isnumeric()}")
print(f"É alfabetico? {algo.isalpha()}")
print(f"É alfanumérico?{algo.isalnum()}")
print(f"Está em letras maíusculas? {algo.isupper()}")
print(f"Está em letras minúsculas? {algo.islower()}")
print(f"Está capitalizada? `{algo.istitle()}")