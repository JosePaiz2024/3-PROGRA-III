class Empleado():

    def __init__(self, nombr, sueldo):
        self.nombr = nombr
        self.sueldo = sueldo

    def info(self):
        return(f"Nombre del empleado: {self.nombr}"+
              f"Sueldo: {self.sueldo}")
        
class Gerente(Empleado):
    def __init__(self, nombr, sueldo,area):
        super().__init__(nombr, sueldo)
        self.area = area

    def info(self):
        infoem= super().info
        print (f"{infoem}  Area: {self.area} ")

gerente = Gerente ("Pepe", 800, "Ventas")
gerente.info()