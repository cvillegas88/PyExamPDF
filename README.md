# PyExamPDF

PyExamPDF es una aplicación interactiva para realizar exámenes desarrollada en Python, utilizando la interfaz gráfica de Tkinter. Permite cargar preguntas desde un archivo PDF y realizar un examen interactivo con retroalimentación inmediata sobre las respuestas.

## Requisitos

Para utilizar Python en sistemas Windows, podrías instalar la aplicación PyCharm en su última versión.

En el caso de los sistemas Linux, instalamos Python desde la terminal.

Además, necesitarás tener algunas librerías específicas instaladas en tu sistema y formatear tu exámen para la correcta lectura del mismo. Aquí tienes una guía paso a paso:

### 1. Instalación de PyCharm en Windows

Accedemos a la página oficial de PyCharm (https://www.jetbrains.com/es-es/pycharm/download/?section=windows), descargamos e instalamos la última versión.

En caso de no tener el gestor de paquetes PIP ya instalado por defecto, deberás instalarlo.

En PyCharm > console
```bash
pip install
```

### 2. Instalación de Python en la mayoría de las distros Linux

1. Actualizamos el sistema:

2. Instalamos Python

Accedemos a la página oficial de PyCharm (https://www.jetbrains.com/es-es/pycharm/download/?section=windows), descargamos e instalamos la última versión.

### 2. Instalar pip

`pip` es el sistema de gestión de paquetes de Python. Aunque suele instalarse automáticamente con Python, puedes verificar su presencia ejecutando el siguiente comando en tu terminal o símbolo del sistema:

```bash
pip --version
```

Si no está instalado, sigue las instrucciones en esta guía para instalarlo.

### 3. Instalar Librerías
Abre tu terminal o símbolo del sistema y ejecuta los siguientes comandos para instalar las librerías necesarias:

```bash
pip install PyPDF2
pip install tk
```

Uso
Ejecuta el script PyExamv_1_7.py para iniciar la aplicación.

La aplicación abrirá una ventana para que ingreses la resolución deseada. Puedes dejarla en blanco y presionar "OK" para usar la resolución predeterminada.

Carga un archivo PDF de preguntas haciendo clic en el botón "Cargar PDF". Selecciona un archivo PDF que contenga preguntas en el formato adecuado.

Inicia el examen haciendo clic en "Iniciar Examen". Responde a las preguntas proporcionando la letra correspondiente a tu elección y haz clic en "Verificar Respuesta".

Al finalizar, haz clic en "Terminar Examen" para obtener un resumen de tu desempeño y exportar los resultados a un archivo CSV.

Estructura del Código
PyExamv_1_7.py: El script principal que inicia la aplicación.
README.md: Este archivo que proporciona información sobre el proyecto.
Otros archivos y carpetas pueden estar presentes dependiendo de la versión y la estructura del código.

Licencia
Este proyecto se distribuye bajo la licencia MIT License. Consulta el archivo LICENSE para obtener más detalles.
