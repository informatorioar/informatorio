# Python Exercises

[Retroceder](../README.md)

This README contains all Python code files from the proyecto4 folder.


## proyecto4.py

```python
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import tkinter as tk

# Crear una ventana simple para probar
ventana: tk.Tk = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("400x200")

ingreso_tarea: tk.Entry = tk.Entry(ventana)
ingreso_tarea.pack()



def agregar_tarea() -> None:
    tarea: str = ingreso_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        ingreso_tarea.delete(0, tk.END)

boton_agregar: tk.Button = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)
boton_agregar.pack()

def eliminar_tarea() -> None:
    seleccion: tuple[int, ...] = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)

boton_eliminar: tk.Button = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
boton_eliminar.pack()

lista_tareas: tk.Listbox = tk.Listbox(ventana)
lista_tareas.pack()

ventana.mainloop()

```

