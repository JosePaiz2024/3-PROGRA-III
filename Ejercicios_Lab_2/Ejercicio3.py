"""Este programa tiene el objetivo de ayudar a un concesionario para la venta de sus vehiculos
muestra las 10 principales caracteristicas de los autos y su precio, pero
para ello, antes se deben de ingresar los datos proximos a mostrar
"""

# Definición de la clase Vehiculo, que representa un automóvil en el concesionario
class Vehiculo:
    def __init__(self, tipo, marca, modelo, año, color, motor, transmision, precio_compra, combustible, pais_origen):
        # Atributos básicos del vehículo
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = motor
        self.transmision = transmision
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()  # Precio de venta calculado automáticamente
        self.combustible = combustible
        self.pais_origen = pais_origen
        self.ruedas = 4  # Todos los vehículos tienen 4 ruedas
        self.capacidad = 5  # Todos los vehículos tienen capacidad para 5 pasajeros

    # Método para calcular el precio de venta basado en un margen de ganancia del 40%
    def calcular_precio_venta(self):
        return self.precio_compra * 1.40

    # Método para mostrar la información completa del vehículo
    def mostrar_informacion(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Combustible: {self.combustible}")
        print(f"País de Origen: {self.pais_origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad: {self.capacidad} pasajeros")
        print("-" * 30)  # Línea separadora para mayor claridad visual


# Función que presenta un menú interactivo al usuario
def menu():
    vehiculos = []  # Lista para almacenar los vehículos registrados

    while True:
        # Opciones del menú
        print("Menú de Concesionario de Autos")
        print("1. Registrar un vehículo")
        print("2. Ver vehículos registrados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Registro de un nuevo vehículo
            tipo = input("Ingrese el tipo de vehículo (Nacional/Importado): ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            año = input("Ingrese el año del vehículo: ")
            color = input("Ingrese el color del vehículo: ")
            motor = input("Ingrese el tipo de motor: ")
            transmision = input("Ingrese el tipo de transmisión: ")
            precio_compra = float(input("Ingrese el precio de compra: "))
            combustible = input("Ingrese el tipo de combustible: ")
            pais_origen = input("Ingrese el país de origen: ")

            # Crear un nuevo objeto Vehiculo con los datos ingresados
            vehiculo = Vehiculo(tipo, marca, modelo, año, color, motor, transmision, precio_compra, combustible, pais_origen)
            vehiculos.append(vehiculo)  # Añadir el vehículo a la lista
            print("¡Vehículo registrado con éxito!\n")

        elif opcion == "2":
            # Visualización de los vehículos registrados
            if vehiculos:
                print("\nVehículos Registrados:")
                for vehiculo in vehiculos:
                    vehiculo.mostrar_informacion()  # Mostrar la información de cada vehículo
            else:
                print("No hay vehículos registrados.\n")

        elif opcion == "3":
            # Salir del programa
            print("¡Gracias por utilizar el sistema!")
            break

        else:
            # Opción no válida
            print("Opción no válida. Por favor, seleccione una opción del menú.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()  # Llamada a la función del menú principal
