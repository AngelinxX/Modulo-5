import informacion

Cantidad_pacientes =int(input("Cuantos pacientes desea ingresar: "))
for i in range (Cantidad_pacientes):
    nombre = input("Ingrese el nombre y apellido: ")
    fecha_nacimiento = input("Ingrese el año de nacimiento: ")
    informacion.agregar_nombre(nombre)
    informacion.agregar_edad(fecha_nacimiento)