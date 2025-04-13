<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1749686400&v=beta&t=hBmszzzG0Zu-m7ZxeCdU5VxgDWqIZuWB0vnrMycuqY4" alt="gabriellugo" />

# GUSANO

<a href="https://github.com/GabrielLugooo/Worm/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Gusano%20Español-000000" alt="Gusano Español" /></a>
<a href="https://github.com/GabrielLugooo/Worm" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Gusano%20Inglés-green" alt="Gusano Inglés" /></a>

### Objetivos

Este proyecto tiene como objetivo demostrar el uso de Python para la automatización de tareas mediante la replicación de archivos. Se centra en la creación de copias de sí mismo para ilustrar el uso de la biblioteca `shutil` y la gestión de argumentos de línea de comandos con `sys`.

A través de este proyecto, los usuarios pueden comprender mejor cómo manipular archivos y directorios en Python, así como gestionar parámetros de entrada para personalizar la ejecución del programa.

### Habilidades Aprendidas

- Manipulación de archivos en Python.
- Uso de la biblioteca `shutil` para copiar archivos.
- Manejo de argumentos de línea de comandos con `sys.argv`.
- Estructura básica de scripts en Python.
- Validación de entrada del usuario.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/shutil-000000?logo=shutil&logoSize=auto)
![Static Badge](https://img.shields.io/badge/sys%20argv-000000?logo=sys.argv&logoSize=auto)

- Python
- `shutil` (biblioteca de Python)
- `sys` (biblioteca de Python)

### Proyecto

#### Vista Previa

<img align="center" src="https://i.imgur.com/21M6lv3.jpeg" alt="Worm1" />
<img align="center" src="https://i.imgur.com/10RHOqZ.jpeg" alt="Worm2" />

#### Código con Comentarios (Español)

```python
# Worm

# El primer argumento es el archivo y el segundo argumento es el número de copias ['worm.py', '2']

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
```

### Limitaciones

El Gusano es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
