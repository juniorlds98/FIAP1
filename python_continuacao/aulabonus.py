#Biblioteca
import random
import os 

palavra = ["bola", "bunda", "paralelepipedo", "manha", "fedido", "advogado", "parecido", "linda", "amarela", "estranho"]
palavraOculta = []
tamanho = len(palavra)

def jogo():
    print ("""
        +---------------------------------------+
        |    Seja bem vindo ao jogo da forca!   |
        +---------------------------------------+
    """)

    #Escolhe uma palavra específica e depois retira ela da string para não se repetir
    palavraSorteada = random.choice(palavra)
    palavra.remove(palavraSorteada)
    
    #Gerar quantidade de letras escondidas de acordo com a quantidade de letras da palavra escondida
    palavraOculta = ["-"] * len(palavraSorteada)
    
    #Variáveis
    lTentativa = 5
    tentativa = 0
    letrasUsadas = []

    while True:
        #O loop sempre começará com o acerto em falso, garantindo que a função seguinte seja ativada
        
        letra = input("Escreva uma letra: ").lower()
        os.system("cls")
        # Identifica quais itens foram usados dentro das variáveis e coloca
        print(f"Você já usou as seguintes letras: {letrasUsadas}")

        #Identifica se o jogador está colocando somente uma letra
        if len(letra) != 1:
            print("Você colocou mais de uma letra, só é possível ser uma!")
            continue
        #Verifica se a letra já foi usada
        if letra in letrasUsadas:
            print("Essa letra já foi escolhida anteriormente por você")
            continue
        
        letrasUsadas.append(letra)
        
        acerto = False

        for i in range(len(palavraSorteada)):
            if palavraSorteada[i] == letra:
                palavraOculta[i] = letra
                acerto = True
        #Caso a letra não seja acertada você perde uma tentativa
        
        if acerto == False:
            #Essa foi a forma mais simples que eu achei de fazer a conta (com um limitador), mas irei procurar outra forma de fazer isso
            tentativa += 1
            print(f"Essa letra não tem na palavra, tente novamente! Você tem {lTentativa-tentativa}") 
        print("Estado atual:"," ".join(palavraOculta))
        
        if tentativa >= lTentativa:
            #Caso mais de 5 tentativas sejam erradas o jogo automaticamente perde e responde qual palavra era
            print(f"Você perdeu, a palavra correta era {palavraSorteada}")
            break

        if "-" not in palavraOculta:
            print(f"Parabens, você acertou a palavra: {palavraSorteada}")
            break
        
def repeticao():
    partidas = 0
    while True:
        jogo()
        partidas += 1
        jogarNovamente = input("Quer jogar novamente? (S/N)").upper()
        if jogarNovamente != "S":
            break
    print ("""
    +---------------------------------------+
    | Que pena, jogue mais vezes! Até logo! |
    +---------------------------------------+
""")
    print (f"Você jogou {partidas} partidas")

if __name__ == "__main__":
    repeticao()