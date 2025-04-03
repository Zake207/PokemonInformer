from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Tamaño inicial y restricciones
        self.setGeometry(100, 100, 600, 450)

        # Título e icono de la ventana
        self.setWindowTitle("Ejemplo de botón")
        self.setWindowIcon(QIcon("./examples/PyQt6/pokeball.png"))

        # Creación del botón básico
        self.boton = QPushButton("Haz clic aquí", self)
        self.boton.setGeometry(50, 50, 200, 40)  # Posición y tamaño
        self.boton.clicked.connect(self.ExampleFunction)

        self.boton.setShortcut("Ctrl+B")
        self.boton.setToolTip("Este es un botón de ejemplo. Presiona Ctrl+B para activarlo.")

        self.boton.setIcon(QIcon("./examples/PyQt6/pokeball.png"))
        self.boton.setIconSize(self.boton.size())  # Ajusta el tamaño del icono

        self.boton.setStyleSheet(
            """
        QPushButton {
                background-color: #3498db;
                color: white;
                border: 2px solid #2980b9;
                border-radius: 10px;
                font-size: 16px;
                padding: 8px 16px;
        }
        QPushButton:hover {
                background-color: #2980b9;
        }
        QPushButton:pressed {
                background-color: #1c6692;
        }
        """
        )

    def ExampleFunction(self):
        print(f"Acción activada")


# Ejecutar la aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
