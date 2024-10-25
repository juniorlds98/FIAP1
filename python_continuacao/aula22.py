# Funções anonimas ou lambda

#sintaxe da função lambda
#lambda arg: expressão

soma = lambda a, b: a+b
print(soma(2,5))


multiplicar = lambda a, b, c: (a+b)*c
print(multiplicar(2, 5, 3))

#Ou

print((lambda a, b: a+b)(3,2))

#Passar funções

r = lambda x, function: x + function(x)
res = r(2, lambda x: x*x)
print(res)
res = r(2, lambda x: x+x)
print(res) 