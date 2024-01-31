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

2.1. Actualizamos el sistema:
```bash
sudo apt update
sudo apt upgrade
```

2.2. Instalamos Python:
```bash
sudo apt install python3
```

2.3. Instalamos PIP:
```bash
sudo apt install python3-pip
```

### 3. Instalar Librerías
Abre tu terminal o símbolo del sistema y ejecuta los siguientes comandos para instalar las librerías necesarias:

```bash
pip install PyPDF2
pip install tk
```

### 4. Formatea tus exámenes
Para que la aplicación pueda cargar de forma correcta tu examen, es necesario formatearlo a una estructura de enunciado, posibles respuestas y respuesta correcta.

A continuación, facilitamos el prompt que debemos ejecutar en ChatGPT para automatizar esta tarea. Cuando obtengamos el resultado final, simplemente debemos añadir la información a un arhivo de texto y exportarlo en formato PDF.

4.1. Preguntas con una única respuesta:
```bash
Prompt:

Te proporciono el siguiente formato de enunciado, posibles respuestas y respuesta correcta para realizar machine learning: 

NEW QUESTION 1
Este es un ejemplo del contexto de una pregunta, donde incluyen datos que debes saber. ¿Esta parte del texto sería la pregunta a responder?

A. Esta sería la posible respuesta uno
B. Esta sería la posible respuesta dos
C. Esta sería la posible respuesta tres 
D. Esta sería la posible respuesta cuatro
F. Esta sería la posible respuesta cinco
G. Esta sería la posible respuesta seis
H. Esta sería la posible respuesta siete
I. Esta sería la posible respuesta ocho

Answer: D 

Necesito que me adaptes a ese mismo formato las siguientes preguntas: 

[Añade tus preguntas con formato distinto]
```

4.2. Preguntas con más de una respuesta:
```bash
Prompt:

Te proporciono el siguiente formato de enunciado, posibles respuestas y respuesta correcta para realizar machine learning: 

NEW QUESTION 1
Este es un ejemplo del contexto de una pregunta, donde incluyen datos que debes saber. ¿Esta parte del texto sería la pregunta a responder?

A. Esta sería la posible respuesta uno
B. Esta sería la posible respuesta dos
C. Esta sería la posible respuesta tres 
D. Esta sería la posible respuesta cuatro
F. Esta sería la posible respuesta cinco
G. Esta sería la posible respuesta seis
H. Esta sería la posible respuesta siete
I. Esta sería la posible respuesta ocho

Answer: A D

Necesito que me adaptes a ese mismo formato las siguientes preguntas: 

[Añade tus preguntas con formato distinto]
```


## Uso
Ejecuta el script PyExamv1.1.8.py para iniciar la aplicación.

La aplicación abrirá una ventana para que ingreses la resolución deseada. Puedes dejarla en blanco y presionar "OK" para usar la resolución predeterminada.

Carga un archivo PDF de preguntas haciendo clic en el botón "Cargar PDF". Selecciona un archivo PDF que contenga preguntas en el formato adecuado.

Inicia el examen haciendo clic en "Iniciar Examen". Responde a las preguntas proporcionando la letra correspondiente a tu elección y haz clic en "Verificar Respuesta".

Al finalizar, haz clic en "Terminar Examen" para obtener un resumen de tu desempeño y exportar los resultados a un archivo CSV.

## Estructura del Código
1. PyExamv1.1.8.py: El script principal que inicia la aplicación.
2. README.md: Este archivo que proporciona información sobre el proyecto.
3. Licencia: Este proyecto se distribuye bajo la licencia MIT License. Consulta el archivo LICENSE para obtener más detalles.
4. Otros archivos y carpetas pueden estar presentes dependiendo de la versión y la estructura del código.
