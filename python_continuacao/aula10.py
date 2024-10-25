# Como usar if

a = 10
b = 5
aux = 0
op = "+"

if op == "+":
    aux = a + b
elif op == "-":
    aux = a - b
elif op == "*":
    aux = a * b
elif op == "/":
    aux = a / b
else:
    print("Sua operação não é valida")

print(str(a) + op + str(b) + " = " + str(aux))