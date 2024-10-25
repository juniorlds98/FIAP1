# Tipo Booleano
aula = True
aula08 = False
aula = 10<15 # Também é um valor boolean

# É possível transformar um valor string em booleano de duas formas
# primeira
aula = "CFB Cursos"

#Strings vazias retornam falso, strings com conteúdo retornam verdadeiro
print(bool(aula))

# segundo

bunda = ""

if bunda:
    print("Possui texto")
else:
    print("Não possui texto")

#Variáveis numéricas retornam verdadeiro ou falso
#Qualquer valor diferente de 0 é considerado True e qualquer valor com 0 é False
#Qualquer valor vazio False qualquer valor True
