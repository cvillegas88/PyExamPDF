# PyExamPDF

PyExamPDF es una aplicación interactiva para realizar exámenes desarrollada en Python, utilizando la interfaz gráfica de Tkinter. Permite cargar preguntas desde un archivo PDF y realizar un examen interactivo con retroalimentación inmediata sobre las respuestas.

## Requisitos

Para utilizar PyExamPDF, necesitarás tener Python y algunas librerías específicas instaladas en tu sistema. Aquí tienes una guía paso a paso:

### 1. Instalar Python

Si no tienes Python instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/). Asegúrate de marcar la opción "Agregar Python al PATH" durante la instalación.

### 2. Instalar pip

`pip` es el sistema de gestión de paquetes de Python. Aunque suele instalarse automáticamente con Python, puedes verificar su presencia ejecutando el siguiente comando en tu terminal o símbolo del sistema:

pip --version

Si no está instalado, sigue las instrucciones en esta guía para instalarlo.

### 3. Instalar Librerías
Abre tu terminal o símbolo del sistema y ejecuta los siguientes comandos para instalar las librerías necesarias:

pip install PyPDF2
pip install tk

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
