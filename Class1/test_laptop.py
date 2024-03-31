from laptop import Laptop
from laptops_gaming import Laptop_Gaming
from laptops_business import Laptop_business

Laptop_pepito = Laptop("lenovo","I7",32)
Laptop_maria = Laptop("lenovo","I7",32,600)

# laptop_juanito =  Laptop_Gaming("MSI","I7",4,"RTX 8GB")

# print(laptop_juanito.realizar_diagnostico_sistema())

laptop_ofi = Laptop_business("Dell","I7",8,550,"6h")

print(laptop_ofi.realizar_diagnostico_sistema())

# for numero in range(1,1000):
#     asus_laptop = Laptop.asus_laptop(numero)
#     print(asus_laptop.__dict__)

# print(Laptop.comparar_costo(Laptop_pepito,Laptop_maria))

# print(Laptop_pepito.__dict__)
# print(Laptop_pepito.valor_final())
# print(f"El valor del descuento:{Laptop_pepito.valor_descuento(10)}")