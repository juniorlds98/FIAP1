# Funções que retornam valores
valores = [1, 5, 3, 2]
def somar(num):
    r=0
    for n in num:
        r+=n
    return r # Return devolve os valores de uma função
print(f"{valores}: soma = {somar(valores)}")