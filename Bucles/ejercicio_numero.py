print(f"Ingresa una lista de datos")
info = input("Ingresa aqui: ")

datos = []
numeros = 0
letras = 0
validacion = False
for i in info:
    validacion = i.isdigit()
    if validacion == False:
        letras += 1
    elif validacion == True:
        numeros += 1
    datos.append(i)

print(f"Su lista es: {datos}")
print(f"Hay {numeros} numeros")
print(f"Hay {letras} Letras")
