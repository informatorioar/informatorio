# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import tkinter as tk

# Crear una ventana simple para probar
ventana: tk.Tk = tk.Tk()
ventana.title("Reloj simple")
ventana.geometry("400x200")

reloj: tk.Label = tk.Label(ventana, font=("Arial", 60),bg="blue", fg="white")

def hora() -> None:
    import time
    hora_actual: str = time.strftime("%H:%M:%S")
    reloj.config(text=hora_actual)
    reloj.after(1000, hora)

reloj.pack(anchor="center", pady=20)

hora()

ventana.mainloop()