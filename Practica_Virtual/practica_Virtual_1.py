
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QLineEdit, QVBoxLayout)
import sys

class miVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear el botón y la caja de texto
        boton = QPushButton("Haz click")
        self.texto = QLineEdit()

        # Crear el layout vertical
        layout = QVBoxLayout()

        # Añadir widgets al layout
        layout.addWidget(boton)
        layout.addWidget(self.texto)

        # Crear el widget central y establecer el layout
        central = QWidget(self)
        central.setLayout(layout)
        self.setCentralWidget(central)

        # Conectar el clic del botón a la función
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_click)

        # Configurar la ventana
        self.setWindowTitle("Mi ventana")
        self.setGeometry(100, 100, 200, 200)

    # Método que se ejecuta cuando se hace clic en el botón
    def boton_click(self):
        print(self.texto.text())

# Inicializar la aplicación y mostrar la ventana
app = QApplication(sys.argv)
ventana = miVentana()
ventana.show()
app.exec()
