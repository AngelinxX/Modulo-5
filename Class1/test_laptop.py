from laptop import Laptop

Laptop_pepito = Laptop("lenovo","I7",32)
Laptop_maria = Laptop("lenovo","I7",32,600)



for numero in range(1,1000):
    asus_laptop = Laptop.asus_laptop(numero)
    print(asus_laptop.__dict__)

# print(Laptop.comparar_costo(Laptop_pepito,Laptop_maria))

# print(Laptop_pepito.__dict__)
# print(Laptop_pepito.valor_final())
# print(f"El valor del descuento:{Laptop_pepito.valor_descuento(10)}")