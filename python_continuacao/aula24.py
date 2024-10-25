#Construtores
# Serve para definir valores de propriedades

class carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self, velocidade, ligado, cor):
        self.velMax = velocidade
        self.ligado = ligado
        self.cor = cor
    def mostrar(self):
        estado = "sim" if self.ligado else "não"
        print(f"velocidade máxima: {self.velMax}")
        print(f"Cor do carro.....: {self.cor}")
        print(f"Ligado...........: {estado}")
        print("----------------------------------")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if(self.ligado):
            print("Andando")
        else:
            print("Carro desligado")
        
c1 = carro(200, False, "Preto")
c2 = carro(120, False, "Branco")
c3 = carro(350, False, "Vermelho")

c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()