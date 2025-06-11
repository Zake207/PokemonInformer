"""
    This module defines the code of the main window of the program.
"""

import sys
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from math import trunc

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # Tamaño inicial y restricciones
        self.setGeometry(100, 100, 600, 450)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(800, 600)

        # Título e icono de la ventana
        self.setWindowTitle("PokeManager")
        self.setWindowIcon(QIcon("./Images/pokeball.png"))
        # Añadir imágenes a la ventana
# Configuración de los botones
        self.pokemon_button = QPushButton("Pokemons", self)
        self.pokemon_button.setGeometry(400, 300, 200, 40)  # Posición y tamaño
        self.pokemon_button.clicked.connect(self.ExampleFunction)

        self.pokemon_button.setShortcut("Ctrl+P")
        self.pokemon_button.setToolTip("Consulta tus pokemons  -  Ctrl+P")

        self.pokemon_button.setIcon(QIcon("./Images/pokebola.png"))
        self.pokemon_button.setIconSize(self.pokemon_button.size())  # Ajusta el tamaño del icono

        self.pokemon_button.setStyleSheet(
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
        
        
        self.team_button = QPushButton("Teams", self)
        self.team_button.setGeometry(400, 350, 200, 40)  # Posición y tamaño
        self.team_button.clicked.connect(self.ExampleFunction)

        self.team_button.setShortcut("Ctrl+T")
        self.team_button.setToolTip("Consulta tus equipos  -  Ctrl+T")

        self.team_button.setIcon(QIcon("./Images/pokebolas.png"))
        self.team_button.setIconSize(self.team_button.size())  # Ajusta el tamaño del icono

        self.team_button.setStyleSheet(
            """
        QPushButton {
                background-color: #66bb6a;
                color: white;
                border: 2px solid #43a047;
                border-radius: 10px;
                font-size: 16px;
                padding: 8px 16px;
        }
        QPushButton:hover {
                background-color: #43a047;
        }
        QPushButton:pressed {
                background-color: #1b5e20;
        }
        """
        )
        
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(400, 400, 200, 40)  # Posición y tamaño
        self.exit_button.clicked.connect(self.ExampleFunction)

        self.exit_button.setShortcut("Ctrl+E")
        self.exit_button.setToolTip("Sal de la Aplicación  -  Ctrl+E")

        self.exit_button.setIcon(QIcon("./Images/apagar.png"))
        self.exit_button.setIconSize(self.team_button.size())  # Ajusta el tamaño del icono

        self.exit_button.setStyleSheet(
            """
        QPushButton {
                background-color: #ef5350;
                color: white;
                border: 2px solid #d32f2f;
                border-radius: 10px;
                font-size: 16px;
                padding: 8px 16px;
        }
        QPushButton:hover {
                background-color: #d32f2f;
        }
        QPushButton:pressed {
                background-color: #b71c1c;
        }
        """
        )

# Configurar una barra de menú
        menu_bar = self.menuBar()  # Crear la barra de menú

        # Primera opcion del menu
        help_menu = menu_bar.addMenu("Ajustes")  # Crear un menú dentro de la barra
        
        config_action = QAction("Configuración", self)  # Crear una acción dentro del menú "Archivo"
        config_action.triggered.connect(self.ExampleFunction)  # Asociar la acción con la función "close()"
        config_action.setShortcut("Ctrl+C")  # Asignar un atajo de teclado a la acción
        config_action.setStatusTip("Configura la aplicación")  # Mensaje de estado al pasar el ratón por encima
        config_action.setIcon(QIcon("./Images/engranajes.png"))  # Icono de la acción
        
        help_action = QAction("Ayuda", self)
        help_action.triggered.connect(self.ExampleFunction)
        help_action.setShortcut("Ctrl+A")
        help_action.setStatusTip("Consulta información sobre la aplicación")
        help_action.setIcon(QIcon("./Images/brujula.png"))

        help_menu.addAction(help_action)
        help_menu.addSeparator()
        help_menu.addAction(config_action)
        
        chatbot_menu = menu_bar.addMenu("ChatBot")
        
        configurate_action = QAction("Configurate", self)
        configurate_action.triggered.connect(self.ExampleFunction)
        configurate_action.setShortcut("Ctrl+Shift+C")
        configurate_action.setStatusTip("Configura el chatbot")
        configurate_action.setIcon(QIcon("./Images/engranajes.png"))
        
        pokemon_action = QAction("Configurate", self)
        pokemon_action.triggered.connect(self.ExampleFunction)
        pokemon_action.setShortcut("Ctrl+Shift+C")
        pokemon_action.setStatusTip("Configura el chatbot")
        pokemon_action.setIcon(QIcon("./Images/engranaje.png"))
        
        team_action = QAction("Configurate", self)
        team_action.triggered.connect(self.ExampleFunction)
        team_action.setShortcut("Ctrl+Shift+C")
        team_action.setStatusTip("Configura el chatbot")
        team_action.setIcon(QIcon("./Images/engranaje.png"))
        
        chatbot_menu.addAction(configurate_action)
        chatbot_menu.addSeparator()
        chatbot_menu.addAction(pokemon_action)
        chatbot_menu.addSeparator()
        chatbot_menu.addAction(team_action)
        
        

        # Hoja de estilo de la ventana, hay opciones para background también
        self.setStyleSheet(
            """
            background-color: #80deea; 
            color: black;
            font-family: Arial, Helvetica, sans-serif;
            font-size: 14px;
            border: 1px solid black;
            padding: 5px;
            """
        )

        # Cargar imagen de fondo y actualizar su tamaño
        self.background = QPixmap("./Images/bg-1.jpg")

    def paintEvent(self, event):
        """
        Dibuja la imagen de fondo escalada al tamaño de la ventana.
        """
        painter = QPainter(self)
        painter.setOpacity(0.8)
        scaled_bg = self.background.scaled(
            self.size(),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        painter.drawPixmap(0, 0, scaled_bg)
        # Adjust button sizes and positions proportionally to the window size
        window_width = self.width()
        window_height = self.height()

        button_width = trunc(window_width * 0.25)
        button_height = trunc(window_height * 0.1)
        button_x = trunc(window_width * 0.37)
        button_y = trunc(window_height * 0.5)
        spacing = trunc(window_height * 0.15)

        self.pokemon_button.setGeometry(button_x, button_y, button_width, button_height)
        self.team_button.setGeometry(button_x, spacing + button_y, button_width, button_height)
        self.exit_button.setGeometry(button_x, 2 * spacing + button_y, button_width, button_height)

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
