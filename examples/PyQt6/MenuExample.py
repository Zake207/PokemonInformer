"""
    This module is a general example about the main window of the project
"""

import sys
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Tamaño inicial y restricciones
        self.setGeometry(100, 100, 600, 450)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)

        # Título e icono de la ventana
        self.setWindowTitle("Pokemon Informer")
        self.setWindowIcon(QIcon("./examples/PyQt6/pokeball.png"))

        # Configurar una barra de menú
        menu_bar = self.menuBar()  # Crear la barra de menú

        # Primera opcion del menu
        file_menu = menu_bar.addMenu("Registro")  # Crear un menú dentro de la barra

        pokemon_action = QAction("Pokemons", self)  # Crear una acción dentro del menú "Archivo"
        pokemon_action.triggered.connect(
            self.ExampleFunction
        )  # Asociar la acción con la función "close()"
        pokemon_action.setShortcut("Ctrl+P")  # Asignar un atajo de teclado a la acción
        pokemon_action.setStatusTip(
            "Consulta tus Pokemon"
        )  # Mensaje de estado al pasar el ratón por encima
        pokemon_action.setIcon(QIcon("./examples/PyQt6/pokebola.png"))  # Icono de la acción

        teams_action = QAction("Teams", self)  # Crear una acción dentro del menú "Archivo"
        teams_action.triggered.connect(self.ExampleFunction)
        teams_action.setShortcut("Ctrl+T")
        teams_action.setIcon(QIcon("./examples/PyQt6/pokebolas.png"))
        teams_action.setStatusTip("Consulta tus equipos")

        file_menu.addAction(teams_action)
        file_menu.addSeparator()
        file_menu.addAction(pokemon_action)

        # Hoja de estilo de la ventana, hay opciones para background también
        self.setStyleSheet(
            """
            background-color: lightblue; 
            color: black;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 14px;
            border: 1px solid black;
            padding: 5px;
            """
        )

        # Cargar imagen de fondo y actualizar su tamaño
        self.background = QPixmap("./examples/PyQt6/bg-1.jpg")

    def paintEvent(self, event):
        """
        Dibuja la imagen de fondo escalada al tamaño de la ventana.
        """
        painter = QPainter(self)
        painter.setOpacity(0.5)
        scaled_bg = self.background.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        painter.drawPixmap(0, 0, scaled_bg)

    def resizeEvent(self, event):
        """
        Se activa cuando la ventana cambia de tamaño, forzando un repintado.
        """
        self.repaint()  # Llama a paintEvent para actualizar el fondo

    def ExampleFunction(self):
        print(f"Acción activada")


# Ejecutar la aplicación
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
