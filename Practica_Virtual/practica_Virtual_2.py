from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class miVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        # Línea para agregar archivos de interfaz
        uic.loadUi('ventana.ui', self)
        self.boton = self.findChild(QtWidgets.QPushButton, "botonClick")
        self.boton.clicked.connect(self.click_boton)

    def click_boton(self):
        print("Botón clickeado")

app = QApplication(sys.argv)
ventana = miVentana()  # Creación de la instancia de miVentana
ventana.show()  # Mostrar la ventana
app.exec()
