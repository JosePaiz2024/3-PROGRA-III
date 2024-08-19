"""Este ejercicio tiene el fin de que una venta de papeleria pueda ingresar productos, los cuales
son cuadernos de 50 o 100 hojas y lapices de colores o grafito, los cuales tendran un precio de 
venta del 30% mas que del precio de compra. La marca de los cuadernos es RAYA y el de 
los lapices es RAYAS"""
# Definición de la clase Articulo
class Articulo:
    def __init__(self, tipo, descripcion, precio_compra):
        self.tipo = tipo  # Tipo de artículo (cuaderno o lápiz)
        self.descripcion = descripcion  # Descripción del artículo
        self.precio_compra = precio_compra  # Precio de compra del artículo
        self.margen_ganancia = 1.30  # Margen de ganancia del 30%
        self.precio_venta = self.calcular_precio_venta()  # Se calcula el precio de venta

    # Método para calcular el precio de venta
    def calcular_precio_venta(self):
        return self.precio_compra * self.margen_ganancia

    # Método para mostrar la información del artículo
    def mostrar_info(self):
        print(f"\nTipo de artículo: {self.tipo}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print()

# Función para registrar un nuevo artículo
def registrar_articulo():
    print("\nRegistro de nuevo artículo")
    tipo = input("Ingrese el tipo de artículo (Cuaderno/Lápiz): ").capitalize()
    
    if tipo == "Cuaderno":
        descripcion = input("Ingrese la cantidad de hojas (50/100): ")
        descripcion = f"Cuaderno HOJITAS de {descripcion} hojas"
    elif tipo == "Lápiz":
        descripcion = input("Ingrese el tipo de lápiz (Grafito/Colores): ")
        descripcion = f"Lápiz RAYAS de {descripcion.lower()}"
    else:
        print("Tipo de artículo no válido.")
        return None

    precio_compra = float(input("Ingrese el precio de compra del artículo: $"))
    return Articulo(tipo, descripcion, precio_compra)

# Función para visualizar los artículos registrados
def visualizar_articulos(articulos):
    if len(articulos) == 0:
        print("\nNo hay artículos registrados.")
    else:
        print("\nArtículos registrados:")
        for articulo in articulos:
            articulo.mostrar_info()

# Función principal del menú
def menu():
    articulos = []
    
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Registrar nuevo artículo")
        print("2. Ver artículos registrados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nuevo_articulo = registrar_articulo()
            if nuevo_articulo:
                articulos.append(nuevo_articulo)
        elif opcion == "2":
            visualizar_articulos(articulos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa
menu()
