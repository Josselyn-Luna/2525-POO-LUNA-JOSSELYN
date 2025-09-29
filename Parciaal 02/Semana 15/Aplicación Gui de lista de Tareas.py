import tkinter as tk
from tkinter import messagebox


class AplicacionListaTareas:
    """
    Clase principal que gestiona la interfaz gráfica de usuario (GUI)
    y la lógica de la aplicación de Lista de Tareas.
    """

    def __init__(self, master):
        # Configuración de la ventana principal
        self.master = master
        master.title("Lista de Tareas - Gemini")
        master.geometry("450x400")  # Establece un tamaño inicial

        # Lista interna para almacenar el estado de las tareas (texto y si está completada)
        # Esto es crucial para la lógica de marcado visual.
        self.tareas = []

        # --- Configuración de Widgets ---

        # 1. Campo de Entrada (Entry) para nuevas tareas
        self.entrada_tarea = tk.Entry(master, width=40, font=('Arial', 10))
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # 2. Botón para Añadir Tarea
        self.btn_anadir = tk.Button(master, text="Añadir Tarea", command=self.anadir_tarea, bg='#4CAF50', fg='white')
        self.btn_anadir.grid(row=0, column=2, padx=5, pady=10)

        # 3. Componente de Lista (Listbox) para mostrar tareas
        # El Listbox almacenará solo el texto visible, la lógica de estado se maneja en 'self.tareas'.
        self.lista_tareas_gui = tk.Listbox(master, height=15, width=60, selectmode=tk.SINGLE, font=('Arial', 10))
        self.lista_tareas_gui.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # 4. Botones de Acción
        self.btn_completar = tk.Button(master, text="Marcar como Completada", command=self.marcar_completada,
                                       bg='#2196F3', fg='white')
        self.btn_completar.grid(row=2, column=0, padx=10, pady=5)

        self.btn_eliminar = tk.Button(master, text="Eliminar Tarea", command=self.eliminar_tarea, bg='#F44336',
                                      fg='white')
        self.btn_eliminar.grid(row=2, column=2, padx=10, pady=5)

        # --- Manejo de Eventos Adicionales ---

        # Permite añadir tarea al presionar la tecla ENTER en el campo de entrada
        self.entrada_tarea.bind('<Return>', lambda event: self.anadir_tarea())

        # Opcional: Permite marcar como completada al hacer doble clic en un elemento de la lista
        self.lista_tareas_gui.bind('<Double-1>', lambda event: self.marcar_completada())

    # ----------------------------------------------------------------------
    # --- Lógica de la Aplicación y Manejadores de Eventos ---
    # ----------------------------------------------------------------------

    def actualizar_lista_gui(self):
        """
        Refresca el Listbox (GUI) basándose en el contenido de la lista interna 'self.tareas'.
        Esto permite aplicar el marcado visual de tareas completadas.
        """
        self.lista_tareas_gui.delete(0, tk.END)  # Borra todo el contenido actual del Listbox

        for i, (texto, completada) in enumerate(self.tareas):
            # Formato condicional: añade un prefijo (✔) si está completada
            display_texto = f"✔ {texto}" if completada else texto
            self.lista_tareas_gui.insert(tk.END, display_texto)

            # Aplica color de fondo gris claro para tareas completadas
            if completada:
                # El Listbox maneja etiquetas (tags) para aplicar estilos
                self.lista_tareas_gui.itemconfig(tk.END, {'bg': '#d9d9d9', 'fg': 'gray'})

    def anadir_tarea(self):
        """
        Manejador de evento para añadir una nueva tarea.
        Se llama al hacer clic en 'Añadir Tarea' o al presionar 'Enter'.
        """
        nueva_tarea = self.entrada_tarea.get().strip()  # Obtiene y limpia el texto de entrada

        if nueva_tarea:
            # Añade la tarea a la lista interna: (texto, estado_completada=False)
            self.tareas.append((nueva_tarea, False))
            self.entrada_tarea.delete(0, tk.END)  # Limpia el campo de entrada
            self.actualizar_lista_gui()
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def marcar_completada(self):
        """
        Manejador de evento para marcar la tarea seleccionada como completada.
        Se llama al hacer clic en 'Marcar como Completada' o al hacer doble clic.
        """
        try:
            # Obtiene el índice de la tarea seleccionada en el Listbox
            indice_seleccionado = self.lista_tareas_gui.curselection()[0]

            # Actualiza el estado de la tarea en la lista interna 'self.tareas'
            texto_actual, estado_actual = self.tareas[indice_seleccionado]
            # Invierte el estado: Si está False, pasa a True; si está True, pasa a False
            nuevo_estado = not estado_actual

            # Reemplaza el elemento en la lista interna con el nuevo estado
            self.tareas[indice_seleccionado] = (texto_actual, nuevo_estado)

            self.actualizar_lista_gui()

        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para marcarla.")

    def eliminar_tarea(self):
        """
        Manejador de evento para eliminar la tarea seleccionada.
        """
        try:
            # Obtiene el índice de la tarea seleccionada
            indice_seleccionado = self.lista_tareas_gui.curselection()[0]

            # Elimina el elemento de la lista interna
            del self.tareas[indice_seleccionado]

            self.actualizar_lista_gui()

        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminarla.")


# ----------------------------------------------------------------------
# --- Ejecución de la Aplicación ---
# ----------------------------------------------------------------------

if __name__ == "__main__":
    # Crea la ventana raíz de Tkinter
    root = tk.Tk()

    # Crea una instancia de la aplicación
    app = AplicacionListaTareas(root)

    # Inicia el bucle principal de eventos de Tkinter
    root.mainloop()