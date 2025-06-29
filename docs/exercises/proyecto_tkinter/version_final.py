# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import tkinter as tk
from tkinter import messagebox
import time

class AplicacionCompleta:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Aplicación Tkinter Completa")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg="#1e1e1e")

        # Variables
        self.tareas = []

        # Configurar interfaz
        self.crear_menu()
        self.crear_reloj()
        self.crear_seccion_tareas()
        self.crear_barra_estado()

        # Forzar actualización de estilos
        self.aplicar_estilos_botones()

        # Iniciar reloj
        self.actualizar_reloj()

    def crear_menu(self):
        """Crear barra de menú con opciones"""
        barra_menu = tk.Menu(self.ventana, bg="#2d2d30", fg="#ffffff",
                            activebackground="#0078d4", activeforeground="#ffffff")
        self.ventana.config(menu=barra_menu)

        # Menú Archivo
        menu_archivo = tk.Menu(barra_menu, tearoff=0, bg="#2d2d30", fg="#ffffff",
                              activebackground="#0078d4", activeforeground="#ffffff")
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Nuevo", command=self.nuevo_archivo)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir_aplicacion)

        # Menú Herramientas
        menu_herramientas = tk.Menu(barra_menu, tearoff=0, bg="#2d2d30", fg="#ffffff",
                                   activebackground="#0078d4", activeforeground="#ffffff")
        barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)

        # Submenú Opciones
        submenu_opciones = tk.Menu(menu_herramientas, tearoff=0, bg="#2d2d30", fg="#ffffff",
                                  activebackground="#0078d4", activeforeground="#ffffff")
        menu_herramientas.add_cascade(label="Opciones", menu=submenu_opciones)
        submenu_opciones.add_command(label="Limpiar tareas", command=self.limpiar_tareas)

        # Menú Ayuda
        menu_ayuda = tk.Menu(barra_menu, tearoff=0, bg="#2d2d30", fg="#ffffff",
                            activebackground="#0078d4", activeforeground="#ffffff")
        barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_acerca_de)

    def crear_reloj(self):
        """Crear sección del reloj en tiempo real"""
        marco_reloj = tk.Frame(self.ventana, bg="#2d2d30", relief=tk.RAISED, bd=2)
        marco_reloj.pack(fill=tk.X, padx=10, pady=(10, 5))

        tk.Label(marco_reloj, text="Hora actual:",
                font=("Arial", 12, "bold"), bg="#2d2d30", fg="#ffffff").pack(pady=5)

        self.etiqueta_reloj = tk.Label(marco_reloj, font=("Arial", 24, "bold"),
                                      bg="#2d2d30", fg="#00d4aa")
        self.etiqueta_reloj.pack(pady=10)

    def crear_seccion_tareas(self):
        """Crear sección de gestión de tareas"""
        marco_tareas = tk.LabelFrame(self.ventana, text="Gestión de Tareas",
                                    font=("Arial", 12, "bold"), bg="#1e1e1e", fg="#ffffff")
        marco_tareas.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Frame para entrada y botones
        marco_entrada = tk.Frame(marco_tareas, bg="#1e1e1e")
        marco_entrada.pack(fill=tk.X, padx=10, pady=10)

        # Entrada de texto
        tk.Label(marco_entrada, text="Nueva tarea:",
                font=("Arial", 10), bg="#1e1e1e", fg="#ffffff").pack(anchor=tk.W)

        self.entrada_tarea = tk.Entry(marco_entrada, font=("Arial", 11), width=40,
                                     bg="#2d2d30", fg="#ffffff", insertbackground="#ffffff")
        self.entrada_tarea.pack(side=tk.LEFT, padx=(0, 10))
        self.entrada_tarea.bind('<Return>', lambda e: self.agregar_tarea())

        # Botones
        self.boton_agregar = tk.Button(marco_entrada, text="Agregar",
                                      command=self.agregar_tarea, bg="#0078d4",
                                      fg="#ffffff", font=("Arial", 10, "bold"),
                                      activebackground="#106ebe", activeforeground="#ffffff",
                                      relief=tk.RAISED, bd=2, cursor="hand2")
        self.boton_agregar.pack(side=tk.LEFT, padx=2)

        self.boton_eliminar = tk.Button(marco_entrada, text="Eliminar",
                                       command=self.eliminar_tarea, bg="#da3b01",
                                       fg="#ffffff", font=("Arial", 10, "bold"),
                                       activebackground="#c13c00", activeforeground="#ffffff",
                                       relief=tk.RAISED, bd=2, cursor="hand2")
        self.boton_eliminar.pack(side=tk.LEFT, padx=2)

        # Lista de tareas con scrollbar
        marco_lista_tareas = tk.Frame(marco_tareas, bg="#1e1e1e")
        marco_lista_tareas.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        scrollbar_tareas = tk.Scrollbar(marco_lista_tareas, bg="#2d2d30", troughcolor="#1e1e1e")
        scrollbar_tareas.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_tareas = tk.Listbox(marco_lista_tareas,
                                      yscrollcommand=scrollbar_tareas.set,
                                      font=("Arial", 10), height=8,
                                      bg="#2d2d30", fg="#ffffff",
                                      selectbackground="#0078d4", selectforeground="#ffffff")
        self.lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_tareas.config(command=self.lista_tareas.yview)

    def crear_barra_estado(self):
        """Crear barra de estado en la parte inferior"""
        self.barra_estado = tk.Label(self.ventana, text="Listo",
                                    relief=tk.SUNKEN, anchor=tk.W,
                                    bg="#2d2d30", fg="#ffffff", font=("Arial", 9))
        self.barra_estado.pack(side=tk.BOTTOM, fill=tk.X)

    def actualizar_reloj(self):
        """Actualizar la hora mostrada en el reloj"""
        hora_actual = time.strftime("%H:%M:%S")
        fecha_actual = time.strftime("%d/%m/%Y")
        self.etiqueta_reloj.config(text=f"{fecha_actual}\n{hora_actual}")
        self.ventana.after(1000, self.actualizar_reloj)

    def agregar_tarea(self):
        """Agregar nueva tarea a la lista"""
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            self.lista_tareas.insert(tk.END, f"• {tarea}")
            self.entrada_tarea.delete(0, tk.END)
            self.tareas.append(tarea)
            self.actualizar_barra_estado(f"Tarea agregada: {tarea}")
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese una tarea válida")

    def eliminar_tarea(self):
        """Eliminar tarea seleccionada de la lista"""
        seleccion = self.lista_tareas.curselection()
        if seleccion:
            indice = seleccion[0]
            tarea_eliminada = self.tareas[indice]
            self.lista_tareas.delete(indice)
            self.tareas.pop(indice)
            self.actualizar_barra_estado(f"Tarea eliminada: {tarea_eliminada}")
        else:
            messagebox.showinfo("Información", "Seleccione una tarea para eliminar")

    def limpiar_tareas(self):
        """Limpiar todas las tareas"""
        if self.tareas:
            respuesta = messagebox.askyesno("Confirmar",
                                          "¿Está seguro de que desea eliminar todas las tareas?")
            if respuesta:
                self.lista_tareas.delete(0, tk.END)
                self.tareas.clear()
                self.actualizar_barra_estado("Todas las tareas han sido eliminadas")
        else:
            messagebox.showinfo("Información", "No hay tareas para eliminar")

    def nuevo_archivo(self):
        """Simular creación de nuevo archivo"""
        self.actualizar_barra_estado("Nuevo archivo creado")

    def salir_aplicacion(self):
        """Cerrar la aplicación"""
        respuesta = messagebox.askyesno("Salir", "¿Está seguro de que desea salir?")
        if respuesta:
            self.ventana.quit()

    def mostrar_acerca_de(self):
        """Mostrar información sobre la aplicación"""
        messagebox.showinfo("Acerca de",
                          "Aplicación Tkinter Completa\n\n"
                          "Combina múltiples funcionalidades:\n"
                          "• Menús desplegables\n"
                          "• Reloj en tiempo real\n"
                          "• Gestión de tareas\n\n"
                          "Desarrollado como ejemplo educativo")

    def actualizar_barra_estado(self, mensaje):
        """Actualizar el mensaje en la barra de estado"""
        self.barra_estado.config(text=mensaje)
        self.ventana.after(3000, lambda: self.barra_estado.config(text="Listo"))

    def aplicar_estilos_botones(self):
        """Forzar la aplicación de estilos a los botones"""
        # Forzar actualización del botón agregar
        self.boton_agregar.config(
            bg="#0078d4", fg="#ffffff",
            activebackground="#106ebe", activeforeground="#ffffff"
        )

        # Forzar actualización del botón eliminar
        self.boton_eliminar.config(
            bg="#da3b01", fg="#ffffff",
            activebackground="#c13c00", activeforeground="#ffffff"
        )

        # Forzar actualización visual
        self.ventana.update_idletasks()

    def ejecutar(self):
        """Iniciar la aplicación"""
        self.ventana.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = AplicacionCompleta()
    app.ejecutar()
