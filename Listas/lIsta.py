#Listas

planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]#se puede trabajar con varios tipos de variables al mismo tiempo

# print(planetas[-3])
# print(planetas[2: 8]) Siempre se ingresa un valor mayor ya que toma el anterior 8 toma valor 7
# print(planetas[2:  ])
# print(len(planetas))
# print(planetas[8]) no existe el indice numero 8 por que va desde el 0

#Trabajar con una lista de numeros

gravedad_en_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus = 124054 #Newtons, en la tierra

print(f"En la Tierra, un autobus de dos pisos pesa {peso_bus} N")
print(f"En Mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_en_planetas[0]} N")

print(f"Lo mas liviano que seria un autobus en el sistema solar es {peso_bus * min (gravedad_en_planetas)} N")
print(f"Lo mas pesado que seria un autobus en el sistema solar es {peso_bus * max (gravedad_en_planetas)} N")