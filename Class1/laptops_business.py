from laptop import Laptop
import random

class Laptop_business(Laptop):
    def __init__(self, marca, procesador, memoria, espacio_de_disco, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.espacio_de_disco = espacio_de_disco
        self.duracion_bateria = duracion_bateria

    def __str__(self) -> str:
        return f"Marca: {self.marca} \n Procesador: {self.procesador} \n Memoria: {self.memoria} \n Espacio de disco: {self.espacio_de_disco} \n Duracion de bateria: {self.duracion_bateria} \n Costo:{self.costo} \n Impuesto: {self.impuesto} \n"

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        resultado_red = self.verificar_conectividad_red()
        resultado_diagnostico["Resultado de Red"] = resultado_red
        return resultado_diagnostico
    
    def verificar_conectividad_red(self):
        resultados = {
            "Wi-Fi": random.choice([True,False]),
            "Acceso a servidores empresariales": random.choice([True,False]),
            "Latencia de la red": random.randint(1,100)
        }
        return resultados
