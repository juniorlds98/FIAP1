import random 
import os #Limpar tela

def jogo():
    tentativas = 0
    sorteado = random.randrange(0, 100)
    print ("""
        +---------------------------------------+
        | Seja bem vindo ao jogo da adivinhação |
        +---------------------------------------+
    """)
    jogador = int(input("Digite o seu número: "))



    while sorteado != jogador:
        os.system("cls")
        if (sorteado > jogador):
            print("O número sorteado é maior")
        elif (sorteado < jogador):
            print("O número sorteado é menor")

        tentativas += 1
        jogador = int(input("Digite o seu número: "))

    print (f"O número é {jogador}, você acertou em {tentativas+1} tentativas")
    

def repeticao():
    partidas = 0
    while True:
        jogo()
        partidas += 1
        jogarNovamente = input("Quer jogar novamente? (S/N)").upper()
        if jogarNovamente != "S":
            break
    print (f"Você jogou {partidas} partidas")
    print ("""
    +---------------------------------------+
    | Que pena, jogue mais vezes! Até logo! |
    +---------------------------------------+
""")

if __name__ == "__main__":
    repeticao()