# Como passar os valores para dentro da função
# É possível passar os valores individualmente ou de forma arbitrária
# Pode criar uma lista de valores e usar 

valores = [1, 5, 3, 2]
def somar(num):
    r = 0
    for n in num:
        r+=n
    print(f"A soma de {r}")

somar(valores)


#argumentos arbitrários
def textos(*t):
    print(t[0])
    print(t[1])
    print(t[2])

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")

#imprimir todos os argumentos
def textos(*txt):
    for t in txt:
        print(t)

textos("CFB Cursos", "Python", "Canal", "Curso", "Computador")

#Caso necessário ele passa o valor padrão dentro do argumento
def carros(c = "Golf"):
    print(f"Modelo: {c}")
carros()