# Worm

# Importar las librerías necesarias
import shutil  # Biblioteca para manipulación de archivos
import sys  # Biblioteca para manejar argumentos de línea de comandos
import tkinter as tk  # Biblioteca para la interfaz gráfica
from tkinter import messagebox

# Función para copiar el archivo
def copiar_archivo():
    try:
        num_copias = int(entry.get())  # Obtener el número de copias desde la entrada
        for num in range(0, num_copias):
            shutil.copy(sys.argv[0], sys.argv[0] + f'{num}.py')
        messagebox.showinfo("Éxito", f"Se han creado {num_copias} copias del archivo.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Crear la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Worm - Generador de Copias")

# Etiqueta y entrada para el número de copias
label = tk.Label(root, text="Número de copias:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Botón para ejecutar la copia
button = tk.Button(root, text="Copiar", command=copiar_archivo)
button.pack()

# Iniciar la interfaz gráfica
root.mainloop()
