# PokemonInformer

Esta aplicación pretende ser una herramienta que permita

## Proposito
+ Profundizar en mis conocimientos sobre python y las aplicaciones de escritorio
+ Aprender las interacciones básicas de una API
+ Aprender a integrar IA en aplicaciones de escritorio
+ Profundizar en herramientas, tecnologías y conceptos genéricos

## Funcionamiento
+ Registro de pokemons (guarda un registro de los pokemon con el diseño que quiera el usuario, permitiendo editarlos o añadirlos)
+ Resgistro de equipos (similar al anterior)
+ Asistente de IA para realizar consultas sobre: pokemon o equipos en concreto siempre pudiendo elegir formato del competitivo y otros parámetros

La persistencia de los datos puede llevarse a cabo a traves de una base de datos o fichero en formato JSON, en caso de usar JSON debería crear una carpeta en el directorio home del usuario para almacenar en diferentes carpetas los diferentes ficheros JSON.

## Documentación
Se usa el módulo de pyhton *Sphinx*, para generar la documentación del código.
**Generación** **

## Desarrollo

### Github
Usar GithubActions para coverall, integración contínua, cloude sonet, etc
Usar el formato de comentarios conventional commits

### Entornos virtuales
El uso de entornos virtuales en sistemas operativos basados en Ubuntu o Debian se complican debido a que estos sistemas tratan todos los entornos virtuales como *externally-managed-enviorment* lo que no permite la instalación de paquetes dentro de estos entornos, por lo que los paquetes en mi máquina ubuntu he de instalarlas. Esto pasa con los entornos virtuales creados por el comando de python3 *python3 -m venv my_venv*, sin embargo, instalar el paquete de python3 *virtualenv* soluciona el problema, permitiendo instalar modulos dentro del entorno virtual.

+ **Creación**            *virtualenv \[nombre_del_entorno\]*
+ **Activación**          *source venv/bin/activate.fish*
+ **Desactivación**       *deactivate*

### Linter
Para poder familiarizarme con más tecnologías tomé la desición de usar un linter, en concreto pylint, el cual ofrece un feedback en forma de puntuación sobre el código, este tiene un fichero de configuración que se crea ejecutando el siguiente comando: *pylint --generate-rcfile > .pylintrc*, cuyas opciones se tienen que estudiar a detalle

Este Linter tiene diferentes modos de ejecución:
+ Sobre un fichero: *pylint \[Ruta/del/fichero\]*
+ Sobre el proyecto: *pylint \[Ruta/del/directorio\]*

### Formater
Para formatear el código se utiliza el módulo de python *black*, debido a que el uso de otras herramientas como prettier me resulto confuso dado a que lo he usado en otros ámbitos. Para formatear el código se debe ejecutar este comando: *black --config pyproject.toml \[Ruta/al/fichero/o/carpeta\]*

El principal problema con este formateador es que si tengo declarada una string demasiado larga este no la dividirá pues la opción que hacía esto se quitó en versiones anteriores a la que estoy usando (25.1.0), por lo que ese problema se debe solucionar a mano.

### Test unitarios
Para realizar las pruebas se utilizará el módulo de python *pytest*, por ningún motivo en particular más que porque es un módulo bastante usado y existen ejemplos de uso y documentación al respecto, otra opción podría ser *unittest*, cómo el objetivo de este proyecto es conocer herramientas de uso común en el desarrollo de código de python no hay una predilección por ninguna en específico.

### PyQt6
El módulo PyQt6, si bien tiene una [documentación](https://doc.qt.io/qtforpython-6/index.html), la considero más adecuada para la comprensión a profundidad del funcionamiento de este. Para un aprendizaje más ágil recurrí a chatgpt para que me generase ejemplos de como funcionan los principales elementos de este módulo, con sus configuraciones, a continuación se enlistan las conversaciones pertinentes a modo de curiosidad.
+ [Ejemplo_1](https://chatgpt.com/share/67ed7818-44c8-8004-a131-7a54d5762494)
+ [Ejemplo_2](https://chatgpt.com/share/67ed7854-abfc-8004-ad6d-f908cad340c4)

## Permisos
Iconos https://www.dariusdan.com/
