

class Laptop:
    def __init__(self, marca, procesador, memoria, costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto

    def valor_descuento(self,descuento):
        return (self.costo * descuento)/100

Laptop_pepito = Laptop("lenovo","I7",32)

print(Laptop_pepito.__dict__)
print(Laptop_pepito.valor_final())
print(f"El valor del descuento:{Laptop_pepito.valor_descuento(10)}")