from reto_auto import auto

auto1=auto("Toyota","Corolla",2022,200000)
auto2=auto("Toyota","Yaris",2024,400000)

for numero in range (1,4):
    auto_toyota = auto.auto_toyota()
    print(auto_toyota.__dict__)

print(auto.comparar_KM(auto1, auto2))

for numero in range(1,4):
    auto_gran_vitara = auto.auto_gran_vitara("Chevrolet")
    print(auto_gran_vitara.__dict__)

for numero in range(1,4):
    auto_gran_vitara = auto.auto_gran_vitara("Suzuki")
    print(auto_gran_vitara.__dict__)

print(auto.comparar_modelo(auto1, auto2))





# auto1=auto("Toyota","Corolla",2022)
# auto1.mostrar_informacion()
# auto1.actualizar_kilometraje(100000)
# auto1.mostrar_informacion()
# auto1.actualizar_kilometraje(3)
# auto1.mostrar_informacion()
# auto1.realizar_viaje(100000)
# auto1.mostrar_informacion()
# auto1.realizar_viaje(-100)
# auto1.mostrar_informacion()
# auto1.estado_auto()