class auto:
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def mostrar_informacion(self):
        print(f"La informacion del auto es: marca {self.marca}, modelo {self.modelo}, año {self.año}, KM {self.kilometraje}")

    def actualizar_kilometraje(self,kilometraje_actual):
        if kilometraje_actual < self.kilometraje:
            print ("No se puede reducir el kilometraje")
        else:
            self.kilometraje = kilometraje_actual
    
    def realizar_viaje(self,kmviaje):
        if kmviaje < 0:
            print ("La cantidad de kilometros debe ser positiva")
        else:
            self.kilometraje += kmviaje
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif self.kilometraje>=20000 and self.kilometraje<100000:
            print("Ya estoy usado")
        else :
            print("Ya dejame descansar por favor")

auto1=auto("Toyota","Corolla",2022)
auto1.mostrar_informacion()
auto1.actualizar_kilometraje(100000)
auto1.mostrar_informacion()
auto1.actualizar_kilometraje(3)
auto1.mostrar_informacion()
auto1.realizar_viaje(100000)
auto1.mostrar_informacion()
auto1.realizar_viaje(-100)
auto1.mostrar_informacion()
auto1.estado_auto()

