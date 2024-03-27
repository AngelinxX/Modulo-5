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

    @classmethod
    def auto_toyota (cls):
        marca = "Toyota"
        modelo = "Yaris"
        año = 2024
        return cls(marca, modelo, año)
    
    @staticmethod
    def comparar_KM (auto1, auto2):
        if auto1.kilometraje ==  auto2.kilometraje:
            return "El kilometraje es similar"
        return "El kilometraje no es similar"

    @classmethod
    def auto_gran_vitara (cls, marca):
        modelo = "Gran Vitara"
        año = 2024
        return cls(marca, modelo, año)
    
    @staticmethod
    def comparar_modelo (auto1, auto2):
        if auto1.modelo ==  auto2.modelo:
            return "El modelo es igual"
        return "El modelo no es igual"
