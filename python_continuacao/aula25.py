#Herança

class NPC: #Classe pai, super ou base
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100


    def info(self):
        print(f"Nome...: {self.nome}")
        print(f"Time...: {self.time}")
        print(f"Força..: {self.forca}")
        print(f"Munição: {self.municao}")
        print(f"Vivo...: {"sim" if self.vivo else "nao"}")
        print(f"Energia: {self.energia}")
        print("-------------------------------------------")

class soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time,self.forca, self.municao)
    
