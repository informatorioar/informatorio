# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import tkinter as tk

# Crear una ventana simple para probar
ventana = tk.Tk()
ventana.title("Barra de desplazamiento")
ventana.geometry("400x200")

marco = tk.Frame(ventana)
marco.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(marco)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

lista = tk.Listbox(marco, yscrollcommand=scrollbar.set, height=10)
for i in range(5):
    lista.insert(tk.END, f"Elemento {i+1}")

lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=lista.yview)


ventana.mainloop()