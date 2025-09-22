import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from datetime import datetime

# Se crea la ventana principal del programa.
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("800x600")

# Lista de eventos (se almacena en memoria).
events = []

# Configuración de estilo.
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TEntry", font=("Helvetica", 10))
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))

# --- Frame de Entrada de Datos ---
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(side=tk.TOP, fill=tk.X)

date_label = ttk.Label(input_frame, text="Fecha:")
date_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
date_entry = DateEntry(input_frame, width=12, background="darkblue", foreground="white", borderwidth=2, locale='es_ES',
                       date_pattern='dd/mm/yyyy')
date_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

time_label = ttk.Label(input_frame, text="Hora (HH:MM):")
time_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
time_entry = ttk.Entry(input_frame, width=10)
time_entry.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

desc_label = ttk.Label(input_frame, text="Descripción:")
desc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
desc_entry = ttk.Entry(input_frame, width=40)
desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

# --- Frame de Botones de Acción ---
button_frame = ttk.Frame(root, padding="10")
button_frame.pack(side=tk.TOP, fill=tk.X)

# --- Frame de Visualización de Eventos (TreeView) ---
tree_frame = ttk.Frame(root, padding="10")
tree_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

columns = ("#1", "#2", "#3")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
tree.pack(fill=tk.BOTH, expand=True)

tree.heading("#1", text="Fecha")
tree.heading("#2", text="Hora")
tree.heading("#3", text="Descripción")

tree.column("#1", width=120, anchor=tk.CENTER)
tree.column("#2", width=80, anchor=tk.CENTER)
tree.column("#3", width=400, anchor=tk.W)


# --- Funciones de Manejo de Eventos ---
def add_event():
    """Agrega un nuevo evento a la lista y actualiza el TreeView."""
    date = date_entry.get()
    time = time_entry.get()
    description = desc_entry.get().strip()

    if not all([date, time, description]):
        messagebox.showwarning("Campos Incompletos", "Por favor, complete todos los campos.")
        return

    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        messagebox.showerror("Formato de Hora Inválido", "Introduzca la hora en formato HH:MM.")
        return

    event_data = (date, time, description)
    events.append(event_data)
    tree.insert("", tk.END, values=event_data)

    time_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    messagebox.showinfo("Evento Agregado", "El evento ha sido agregado correctamente.")


def delete_event():
    """Elimina el evento seleccionado después de una confirmación."""
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selección Vacía", "Seleccione un evento para eliminar.")
        return

    if messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este evento?"):
        event_values_tuple = tree.item(selected_item[0], 'values')

        try:
            events.remove(event_values_tuple)
            tree.delete(selected_item[0])
            messagebox.showinfo("Evento Eliminado", "El evento ha sido eliminado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "No se pudo encontrar el evento.")


# Botones con sus comandos
add_button = ttk.Button(button_frame, text="Agregar Evento", command=add_event)
add_button.pack(side=tk.LEFT, padx=5)

delete_button = ttk.Button(button_frame, text="Eliminar Evento Seleccionado", command=delete_event)
delete_button.pack(side=tk.LEFT, padx=5)

exit_button = ttk.Button(button_frame, text="Salir", command=root.quit)
exit_button.pack(side=tk.RIGHT, padx=5)

# Bucle principal para mantener la ventana abierta
root.mainloop()