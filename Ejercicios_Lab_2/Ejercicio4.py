"""En esta ocasión, el programa le ayuda a un almacen electronico a registrar las 6 principales
caracteristicas que tienen tres dispositivos(celulares, tablets y portatiles), que
basicamente son los que vende."""

class ProductoElectronico:
    def __init__(self, nombre, precio_compra, caracteristicas):
        """
        Inicializa un nuevo producto electrónico con sus características.
         Nombre del producto
         Precio de compra del producto
         Lista con las 6 principales características del producto
        """
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.caracteristicas = caracteristicas

    def calcular_precio_venta(self):
        """
        Calcula el precio de venta basado en el precio de compra multiplicado por 1.7.
        y retorna Precio de venta
        """
        margen_ganancia = 1.7
        return self.precio_compra * margen_ganancia

    def mostrar_info(self):
        """
        Muestra la información del producto, incluyendo sus características y precio de venta.
        """
        print(f"\nNombre del producto: {self.nombre}")
        print("Características:")
        for i, caracteristica in enumerate(self.caracteristicas, 1):
            print(f"  {i}. {caracteristica}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.calcular_precio_venta():.2f}")

def ingresar_producto():
    """
    Solicita al usuario la información del producto y retorna una instancia de ProductoElectronico.
    y retiorna Instancia de ProductoElectronico con los datos ingresados
    """
    nombre = input("Ingrese el nombre del producto: ")
    precio_compra = float(input("Ingrese el precio de compra del producto: "))
    
    print("Ingrese las 6 características del producto:")
    caracteristicas = [input(f"Característica {i+1}: ") for i in range(6)]
    
    return ProductoElectronico(nombre, precio_compra, caracteristicas)

def mostrar_menu():
    """
    Muestra el menú principal y maneja las opciones seleccionadas por el usuario.
    """
    productos = []
    
    while True:
        print("\nMenú de opciones:")
        print("1. Registrar nuevo dispositivo")
        print("2. Ver productos registrados")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            # Registrar nuevo dispositivo
            num_productos = int(input("¿Cuántos productos desea ingresar? "))
            for _ in range(num_productos):
                producto = ingresar_producto()
                productos.append(producto)
        
        elif opcion == '2':
            # Mostrar productos registrados
            if not productos:
                print("No hay productos registrados.")
            else:
                for producto in productos:
                    producto.mostrar_info()
        
        elif opcion == '3':
            # Salir del programa
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el menú principal
mostrar_menu()
