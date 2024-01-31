import PyPDF2
import re
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog

class PyExamApp:
    def __init__(self, root):
        # Inicialización de la aplicación y configuración de la interfaz gráfica
        self.root = root
        self.root.title("PyExamPDF")

        # Preguntar al usuario sobre la resolución
        self.ask_resolution()

        # Inicialización de variables de la aplicación
        self.ruta_pdf = ""
        self.examen_generado = []
        self.respuestas_correctas = []
        self.indice_pregunta = 0
        self.aciertos = 0
        self.fallos = 0
        self.total_respondidas = 0

        # Aplicar un tema visual
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Crear el marco principal
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        # Texto para mostrar la pregunta actual
        self.texto_pregunta = tk.Text(self.main_frame, wrap='word', font=('Arial', 12))
        self.texto_pregunta.grid(row=0, column=0, columnspan=2, pady=(10, 5), padx=(10, 5), sticky="nsew")

        # Entrada para la respuesta del usuario
        self.entry_respuesta = tk.Entry(self.main_frame, font=('Arial', 12), width=2)  # Ajusta el ancho según tus preferencias
        self.entry_respuesta.grid(row=1, column=0, pady=(5, 10), padx=(10, 5), sticky="nsew")

        # Configurar validación para aceptar solo "a", "b", "c", "d", "e", "f", "g", "h" o "i"
        vcmd = (root.register(self.validate_respuesta), '%S')
        self.entry_respuesta.config(validate='key', validatecommand=vcmd)

        # Lista para almacenar las respuestas del usuario
        self.respuestas_usuario = []

        # Botón para verificar la respuesta
        self.btn_verificar_respuesta = ttk.Button(self.main_frame, text="Verificar Respuesta", command=self.verificar_respuesta, state=tk.DISABLED)
        self.btn_verificar_respuesta.grid(row=1, column=1, pady=(5, 10), padx=(5, 10), sticky="nsew")

        # Marco para el score
        self.score_frame = ttk.LabelFrame(self.main_frame, text="")
        self.score_frame.grid(row=2, column=0, columnspan=2, pady=(10, 5), padx=(10, 5), sticky="nsew")

        # Etiqueta para mostrar el score
        self.lbl_score = ttk.Label(self.score_frame, text="Aciertos: 0, Fallos: 0, Porcentaje: 0%, Total Respondidas: 0", font=('Arial', 12))
        self.lbl_score.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Botón para cargar el PDF
        self.btn_cargar_pdf = ttk.Button(self.main_frame, text="Cargar PDF", command=self.cargar_pdf)
        self.btn_cargar_pdf.grid(row=3, column=0, pady=10, padx=(10, 5), sticky="nsew")

        # Botón para iniciar el examen
        self.btn_iniciar_examen = ttk.Button(self.main_frame, text="Iniciar Examen", command=self.iniciar_examen, state=tk.DISABLED)
        self.btn_iniciar_examen.grid(row=3, column=1, pady=10, padx=(5, 10), sticky="nsew")

        # Botón para terminar el examen
        self.btn_terminar_examen = ttk.Button(self.main_frame, text="Terminar Examen", command=self.terminar_examen, state=tk.NORMAL)
        self.btn_terminar_examen.grid(row=4, column=0, columnspan=2, pady=(10, 20), padx=(10, 5), sticky="nsew")

        # Configurar pesos de la fila y columna para que se expandan
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.main_frame.rowconfigure(4, weight=1)

        # Manejar eventos de cambio de tamaño de ventana
        self.root.bind("<Configure>", self.handle_resize)

    def ask_resolution(self):
        # Preguntar al usuario sobre la resolución
        resolution = simpledialog.askstring("Resolución", "Ingresa tu resolución (por ejemplo, 800x600). Para dejar por defecto, pulsa OK ")
        if resolution:
            width, height = map(int, resolution.split('x'))
            self.root.geometry(f"{width}x{height}")

    def cargar_pdf(self):
        self.ruta_pdf = filedialog.askopenfilename(title="Seleccionar PDF", filetypes=[("PDF files", "*.pdf")])
        if self.ruta_pdf:
            self.examen_generado, self.respuestas_correctas = self.generar_examen(self.ruta_pdf)
            if self.examen_generado:
                self.btn_iniciar_examen["state"] = tk.NORMAL
                self.btn_verificar_respuesta["state"] = tk.DISABLED  # Deshabilitar Verificar Respuesta
                self.btn_terminar_examen["state"] = tk.NORMAL  # Habilitar Terminar Examen
                messagebox.showinfo("Éxito", "PDF cargado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo cargar el PDF.")
                self.reset_buttons()  # Restaurar el estado de los botones solo si no hay preguntas cargadas

    def reset_buttons(self):
        # Restaurar el estado de los botones a "deshabilitado"
        self.btn_iniciar_examen["state"] = tk.DISABLED
        self.btn_verificar_respuesta["state"] = tk.DISABLED
        self.btn_terminar_examen["state"] = tk.DISABLED

    def generar_examen(self, ruta_pdf):
        try:
            with open(ruta_pdf, "rb") as archivo_pdf:
                lector_pdf = PyPDF2.PdfReader(archivo_pdf)
                contenido = ""
                for pagina in range(len(lector_pdf.pages)):
                    contenido += lector_pdf.pages[pagina].extract_text()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el PDF: {str(e)}")
            return [], []

        # Se ha modificado el patrón para incluir más respuestas (hasta I) y permitir varias respuestas.
        patron_pregunta = re.compile(r'(?i)(NEW QUESTION \d+.*?)([A-I]+\. .*?Answer: [A-I ]+)', re.DOTALL)

        matches = patron_pregunta.finditer(contenido)
        examen_generado = []
        respuestas_correctas = []

        for match in matches:
            pregunta = match.group(1) + match.group(2)
            examen_generado.append(pregunta)

            # Modificación para manejar múltiples respuestas
            respuestas = re.findall(r'[A-I]', match.group(2).split("Answer: ")[1])
            respuestas_correctas.append(set(respuestas))  # Convertir a conjunto para facilitar la comparación

        return examen_generado, respuestas_correctas

    def iniciar_examen(self):
        self.indice_pregunta = 0
        self.aciertos = 0
        self.fallos = 0
        self.total_respondidas = 0
        self.mostrar_pregunta()
        # Habilitar el botón de "Verificar Respuesta" al iniciar el examen
        self.btn_verificar_respuesta["state"] = tk.NORMAL

    def mostrar_pregunta(self):
        if 0 <= self.indice_pregunta < len(self.examen_generado):
            pregunta_actual = self.examen_generado[self.indice_pregunta].rsplit('Answer:', 1)[0]
            self.texto_pregunta.delete(1.0, tk.END)
            self.texto_pregunta.insert(tk.END, pregunta_actual)
        else:
            # Mostrar el resumen de resultados al finalizar el examen
            porcentaje = (self.aciertos / self.total_respondidas) * 100 if self.total_respondidas > 0 else 0
            resumen = f"Fin del examen\nPreguntas Respondidas: {self.total_respondidas}\nAciertos: {self.aciertos}, Fallos: {self.fallos}, Porcentaje de aciertos: {porcentaje:.2f}%"
            self.texto_pregunta.delete(1.0, tk.END)
            self.texto_pregunta.insert(tk.END, resumen)

        self.entry_respuesta.delete(0, tk.END)

    def validate_respuesta(self, s):
        # Función de validación para aceptar solo "a", "b", "c", "d", "e", "f", "g", "h" o "i"
        return s.lower() in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

    def verificar_respuesta(self):
        if self.indice_pregunta >= 0:  # Verificar si el examen está iniciado
            if 0 <= self.indice_pregunta < len(self.examen_generado):
                respuesta_usuario = self.entry_respuesta.get().upper()

                # Verificar si la respuesta no está vacía
                if not respuesta_usuario:
                    messagebox.showwarning("Respuesta Vacía", "Por favor, ingresa una respuesta antes de verificar.")
                    return

                respuestas_correctas = set(self.respuestas_correctas[self.indice_pregunta])

                # Convertir respuestas del usuario a un conjunto
                respuestas_usuario = set(respuesta_usuario)

                if respuestas_usuario == respuestas_correctas:
                    self.aciertos += 1
                    messagebox.showinfo("Correcto", "Respuesta correcta.")
                else:
                    self.fallos += 1
                    messagebox.showerror("Incorrecto", "Respuesta incorrecta. Inténtalo de nuevo.")

                self.total_respondidas += 1
                self.indice_pregunta += 1
                self.mostrar_pregunta()
                self.respuestas_usuario.append(respuesta_usuario)  # Agregar la respuesta del usuario a la lista

                porcentaje = (self.aciertos / self.total_respondidas) * 100 if self.total_respondidas > 0 else 0
                self.lbl_score["text"] = f"Aciertos: {self.aciertos}, Fallos: {self.fallos}, Porcentaje: {porcentaje:.2f}%, Total Respondidas: {self.total_respondidas}"

            else:
                messagebox.showinfo("Fin del Examen", "Has completado el examen. ¡Bien hecho!")
        else:
            messagebox.showwarning("Iniciar Examen", "Debes iniciar el examen antes de verificar respuestas.")

    def terminar_examen(self):
        porcentaje = (self.aciertos / self.total_respondidas) * 100 if self.total_respondidas > 0 else 0
        mensaje = f"¡Examen terminado!\nPreguntas Respondidas: {self.total_respondidas}, Aciertos: {self.aciertos}, Fallos: {self.fallos}\nPorcentaje de aciertos: {porcentaje:.2f}%"

        # Mostrar el resumen en una ventana emergente
        messagebox.showinfo("Fin del Examen", mensaje)

        # Exportar resultados a CSV
        self.exportar_resultados('resultados.csv')

        self.root.destroy()

    def exportar_resultados(self, filename):
        # Crear un archivo CSV y escribir los resultados
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Pregunta', 'Respuesta Correcta', 'Respuesta Usuario', 'Correcto'])
            for i, pregunta in enumerate(self.examen_generado):
                respuesta_correcta = self.respuestas_correctas[i]
                respuesta_usuario = '' if i >= len(self.respuestas_usuario) else self.respuestas_usuario[i]
                correcto = respuesta_correcta == respuesta_usuario
                writer.writerow([pregunta, respuesta_correcta, respuesta_usuario, correcto])

    def handle_resize(self, event):
        # Manejar eventos de cambio de tamaño de ventana aquí
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PyExamApp(root)
    root.mainloop()
