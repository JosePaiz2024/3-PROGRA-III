"""Este ejercicio personal, tiene el fin de resolver una problematica 
de Agenda de contactos personales, en donde registramos el contacto y
mostramos los exixtentes"""

class Contacto:
    def __init__(self, nombre, telefono, correo):
        """
        Inicializa un nuevo contacto con los datos:
        Nombre del contacto
        Número de teléfono del contacto
        Correo electrónico del contacto
        """
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        """
        Representa el contacto en formato de cadena.
        """
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"

class Agenda:
    def __init__(self):
        """
        Inicializa una nueva agenda con una lista vacía de contactos.
        """
        self.contactos = []

    def agregar_contacto(self, contacto):
        """
        Agrega un contacto a la lista de contactos.
        
        """
        self.contactos.append(contacto)

    def listar_contactos(self):
        """
        Muestra la información de todos los contactos en la agenda.
        """
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto)

def mostrar_menu():
    """
    Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
    """
    agenda = Agenda()
    
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar contacto")
        print("2. Listar contactos")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            # Agregar nuevo contacto
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono del contacto: ")
            correo = input("Ingrese el correo electrónico del contacto: ")
            contacto = Contacto(nombre, telefono, correo)
            agenda.agregar_contacto(contacto)
            print(f"Contacto '{nombre}' agregado a la agenda.")
        
        elif opcion == '2':
            # Listar contactos
            agenda.listar_contactos()
        
        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú principal
mostrar_menu()