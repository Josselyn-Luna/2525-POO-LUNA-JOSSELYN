import tkinter as tk
from tkinter import ttk


# --- Función para agregar un elemento a la lista ---
def agregar_item():
    """
    Obtiene el texto del campo de entrada y lo agrega a la lista (ListBox).
    """
    # Obtener el texto del campo de entrada
    item = entry_texto.get()

    # Verificar que el campo no esté vacío
    if item:
        # Agregar el texto al final de la lista
        lista_datos.insert(tk.END, item)
        # Limpiar el campo de entrada después de agregar
        entry_texto.delete(0, tk.END)


# --- Función para limpiar la lista y el campo de texto ---
def limpiar_todo():
    """
    Borra todos los elementos de la lista y el contenido del campo de entrada.
    """
    # Eliminar todos los elementos de la lista, desde el inicio (0) hasta el final (tk.END)
    lista_datos.delete(0, tk.END)

    # Limpiar el campo de entrada
    entry_texto.delete(0, tk.END)


# --- Configuración de la ventana principal ---
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño inicial de la ventana

# --- Diseño de la Interfaz con Widgets ---
# Crear y colocar una etiqueta de título
label_titulo = ttk.Label(ventana, text="Gestor de Tareas", font=("Arial", 16, "bold"))
label_titulo.pack(pady=10)  # pady agrega espacio vertical

# --- Marco para los controles de entrada (Entry y Botones) ---
frame_entrada = ttk.Frame(ventana)
frame_entrada.pack(pady=5)

# Crear un campo de entrada de texto
entry_texto = ttk.Entry(frame_entrada, width=30)
entry_texto.pack(side=tk.LEFT, padx=5)

# Crear el botón "Agregar" y asociarlo a la función agregar_item
btn_agregar = ttk.Button(frame_entrada, text="Agregar", command=agregar_item)
btn_agregar.pack(side=tk.LEFT, padx=5)

# --- Lista para mostrar los datos ---
# Crear un marco para la lista
frame_lista = ttk.Frame(ventana)
frame_lista.pack(pady=10, fill=tk.BOTH, expand=True)

# Crear una lista (ListBox) para mostrar los datos
lista_datos = tk.Listbox(frame_lista)
lista_datos.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

# Añadir un scrollbar a la lista para manejar más elementos
scrollbar = ttk.Scrollbar(frame_lista, orient="vertical", command=lista_datos.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")
lista_datos.config(yscrollcommand=scrollbar.set)

# --- Botón para limpiar ---
# Crear el botón "Limpiar" y asociarlo a la función limpiar_todo
btn_limpiar = ttk.Button(ventana, text="Limpiar Todo", command=limpiar_todo)
btn_limpiar.pack(pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()