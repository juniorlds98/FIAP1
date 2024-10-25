#Classes
# É a especificações de um objetivo, serve como regras

class carro:
    velMax = 0
    ligado = False
    cor = ""

c1 = carro()
c2 = carro()
c3 = carro()

c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False

estado = "sim" if c1.ligado else "não"

print(f"velocidade máxima: {c1.velMax}")
print(f"Cor do carro: {c1.cor}")
print(f"Ligado: {estado}")