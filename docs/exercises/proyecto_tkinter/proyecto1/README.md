# Python Exercises

[Retroceder](../README.md)

This README contains all Python code files from the proyecto1 folder.


## proyecto1.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import tkinter as tk

# Crear una ventana simple para probar
ventana: tk.Tk = tk.Tk()
ventana.title("Menu Desplegable")
ventana.geometry("400x200")

barra_menu: tk.Menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_principal: tk.Menu = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Principal", menu=menu_principal)

submenu: tk.Menu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Opciones", menu=submenu)

submenu.add_command(label="Opción 1")
submenu.add_command(label="Opción 2")

ventana.mainloop()
```

