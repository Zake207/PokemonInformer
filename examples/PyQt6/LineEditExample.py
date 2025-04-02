import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuramos el layout vertical
        layout = QVBoxLayout(self)

        # Creamos un QLineEdit para entrada de texto
        self.entrada_texto = QLineEdit(self)
        self.entrada_texto.setPlaceholderText("Ingresa un texto aquí")

        # Creamos un botón que realizará una acción con el texto
        self.boton = QPushButton("Procesar Texto", self)
        self.boton.clicked.connect(self.procesar_texto)

        # Agregamos los widgets al layout
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.boton)

        # Configuramos la ventana
        self.setWindowTitle("Ejemplo de QLineEdit en PyQt6")
        self.resize(300, 100)

    def procesar_texto(self):
        # Obtenemos el texto ingresado
        texto = self.entrada_texto.text()
        # Realizamos alguna operación (en este caso, imprimir en consola)
        print(texto, "pista: sí")
        self.entrada_texto.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
