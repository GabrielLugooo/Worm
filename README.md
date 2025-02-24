<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1744243200&v=beta&t=oXX-ixT9bR3dJcYCLv4KBs5wjKFoeP0524kFGHQMYmQ" alt="gabriellugo" />

# WORM

<a href="https://github.com/GabrielLugooo/Worm" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Worm-000000" alt="English Worm" /></a>
<a href="https://github.com/GabrielLugooo/Worm/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Worm-green" alt="Spanish Worm" /></a>

### Objective

This project aims to demonstrate the use of Python for task automation by replicating files. It focuses on self-replication to illustrate the use of the `shutil` library and command-line argument management with `sys`.

Through this project, users can better understand how to manipulate files and directories in Python, as well as handle input parameters to customize the program execution.

### Skills Learned

- File manipulation in Python.
- Use of the `shutil` library to copy files.
- Command-line argument handling with `sys.argv`.
- Basic structure of Python scripts.
- User input validation.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)

- Python
- `shutil` (Python library)
- `sys` (Python library)

### Project

#### Preview

<img align="center" src="https://i.imgur.com/21M6lv3.jpeg" alt="Worm1" />
<img align="center" src="https://i.imgur.com/10RHOqZ.jpeg" alt="Worm2" />

#### Code with Comments (English)

```python
# Worm

# First argument is the file and second argument is the number of copies ['worm.py', '2']

# Import the necessary libraries
import shutil # Library for file manipulation
import sys # Library for handling command line arguments
import tkinter as tk # Library for the graphical interface
from tkinter import messagebox

# Function to copy the file
def copy_file():
try:
num_copies = int(entry. get()) # Get the number of copies from the input
for num in range(0, num_copies):
shutil. copy(sys.argv[0], sys.argv[0] + f'{num}.py')
messagebox. showinfo("Success", f"{num_copies} copies of the file have been created.")
except ValueError:
messagebox. showerror("Error", "Please Please enter a valid number.")

# Create the graphical interface window
root = tk.Tk()
root.title("Worm - Copy Generator")

# Label and entry for the number of copies
label = tk.Label(root, text="Number of copies:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Button to run the copy
button = tk.Button(root, text="Copy", command=copy_file)
button.pack()

# Start the graphical interface
root.mainloop()
```

### Limitations

Worm it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
