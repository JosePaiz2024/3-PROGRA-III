class Animal():
    def __init__(self, estado):
        self.estado = estado

class Perro(Animal):
    def __init__(self, estado, nombre):
        super().__init__(estado)
        self.nombre = nombre

# Solicitar al usuario que ingrese los valores
estado = input("Ingrese el estado del perro: ")
nombre = input("Ingrese el nombre del perro: ")

# Crear el objeto Perro con los valores ingresados
perrito = Perro(estado, nombre)

# Imprimir los valores
print(f"Estado del perro: {perrito.estado}")
print(f"Nombre del perro: {perrito.nombre}")