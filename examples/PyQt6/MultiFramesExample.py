import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
    QLabel,
)


class PaginaUno(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel("Esta es la Página 1")
        self.boton = QPushButton("Ir a la Página 2")
        layout.addWidget(self.label)
        layout.addWidget(self.boton)


class PaginaDos(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.label = QLabel("Esta es la Página 2")
        self.boton = QPushButton("Volver a la Página 1")
        layout.addWidget(self.label)
        layout.addWidget(self.boton)


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de Múltiples Frames")
        self.resize(400, 200)

        # Creamos un QStackedWidget para contener las páginas
        self.stacked_widget = QStackedWidget(self)

        # Instanciamos las páginas
        self.pagina_uno = PaginaUno(self)
        self.pagina_dos = PaginaDos(self)

        # Agregamos las páginas al QStackedWidget
        self.stacked_widget.addWidget(self.pagina_uno)
        self.stacked_widget.addWidget(self.pagina_dos)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        # Conectamos los botones para cambiar de página
        self.pagina_uno.boton.clicked.connect(self.mostrar_pagina_dos)
        self.pagina_dos.boton.clicked.connect(self.mostrar_pagina_uno)

    def mostrar_pagina_dos(self):
        self.stacked_widget.setCurrentWidget(self.pagina_dos)

    def mostrar_pagina_uno(self):
        self.stacked_widget.setCurrentWidget(self.pagina_uno)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
