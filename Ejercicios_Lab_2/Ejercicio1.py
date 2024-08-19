"""El programa registra la información básica de un perro 
en una veterinaria, con 8 caracteristicas del animal, cuando el perro 
llega, su estado es no atendido, pero cuando se registran
su estado cambia a atendido, además que se etiende a perros 
respectivo a su peso  como grandes(+10kg) y pequeños (-10kg)"""

# Clase para representar a un perro
class Perro:
    # Constructor de la clase, inicializa las características del perro
    def __init__(self, nombre, raza, edad, peso, color, sexo, nombre_dueno, direccion_dueno):
        self.nombre = nombre  # Nombre del perro
        self.raza = raza  # Raza del perro
        self.edad = edad  # Edad del perro
        self.peso = peso  # Peso del perro
        self.color = color  # Color del pelaje del perro
        self.sexo = sexo  # Sexo del perro (macho/hembra)
        self.nombre_dueno = nombre_dueno  # Nombre del dueño del perro
        self.direccion_dueno = direccion_dueno  # Dirección del dueño del perro
        self.estado = "NO ATENDIDO"  # Estado inicial del perro al llegar a la veterinaria

    # Método para registrar al perro, cambiando su estado a "ATENDIDO"
    def registrar(self):
        self.estado = "ATENDIDO"  # Cambia el estado del perro a "ATENDIDO"
        # Clasifica al perro según su peso como "Perro Grande" o "Perro Pequeño"
        if self.peso < 10:
            tamano = "Perro Pequeño"
        else:
            tamano = "Perro Grande"
        # Muestra la información del perro en pantalla
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg ({tamano})")
        print(f"Color: {self.color}")
        print(f"Sexo: {self.sexo}")
        print(f"Nombre del dueño: {self.nombre_dueno}")
        print(f"Dirección del dueño: {self.direccion_dueno}")
        print(f"Estado: {self.estado}")

# Función para ingresar las características del perro
def ingresar_datos_perro():
    nombre = input("Ingrese el nombre del perro: ")
    raza = input("Ingrese la raza del perro: ")
    edad = int(input("Ingrese la edad del perro (en años): "))
    peso = float(input("Ingrese el peso del perro (en kg): "))
    color = input("Ingrese el color del perro: ")
    sexo = input("Ingrese el sexo del perro (Macho/Hembra): ")
    nombre_dueno = input("Ingrese el nombre del dueño: ")
    direccion_dueno = input("Ingrese la dirección del dueño: ")
    #Esta linea nos ayudara a ver la division de los datos registradosjs
    print("___________________________________________________________\n")
    print(f"Datos de {nombre}")

    return Perro(nombre, raza, edad, peso, color, sexo, nombre_dueno, direccion_dueno)

# Ejemplo de uso del programa
mi_perro = ingresar_datos_perro()  # Se ingresan las características del perro
mi_perro.registrar()  # Se registra al perro y se muestra su información
