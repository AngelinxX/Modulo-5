nombre_paciente=[]
def agregar_nombre(nombre):
    nombre_paciente.append(nombre)
    print(f"Los nombres de los pacientes {nombre_paciente} ")

edad_paciente=[]
def agregar_edad(fecha_nacimiento):
    edad_actual = 2024 - int(fecha_nacimiento)
    edad_paciente.append(edad_actual)
    print(f"La edad de los pacientes {edad_paciente} ")
    edad_max = max(edad_paciente)
    indice_max = edad_paciente.index(edad_max)
    mayor = nombre_paciente[indice_max]
    print(f"La persona con mayor edad es {mayor} con edad {edad_max}")

    edad_min = min(edad_paciente)
    indice_min = edad_paciente.index(edad_min)
    menor = nombre_paciente[indice_min]
    print(f"La persona con menor edad es {menor} con edad {edad_min}")



