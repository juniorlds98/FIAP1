# Como usar if e else

clima = "sol"
dinheiro = 650
lugar = "vazio"
# o operador and precisa que as duas condições sejam verdadeiras para devolver um valor True
# o operador or precisa que somente uma das condições sejam verdadeiras para devolver um valor True
if clima == "sol" or (dinheiro >= 300 and dinheiro <= 500):
    lugar = "clube"
else:
    lugar = "cinema"

print("Vou ao "+lugar)