# Archivo: producto.py

class Producto:
    """
    Clase que representa un producto en el inventario.
    Atributos:
        - id: Identificador único del producto.
        - nombre: Nombre del producto.
        - cantidad: Cantidad disponible en stock.
        - precio: Precio unitario del producto.
    """

    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos "getters" para acceder a los atributos
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Métodos "setters" para modificar los atributos
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def __str__(self):
        """
        Método especial para representar el objeto como una cadena de texto.
        Útil para imprimir información del producto de forma clara.
        """
        return (f"ID: {self.id} | Nombre: {self.nombre} | "
                f"Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}")

    def to_csv_line(self):
        """
        Convierte los datos del producto a una línea de texto CSV.
        """
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}\n"

# Archivo: inventario.py
# Importa la clase Producto si la tienes en un archivo separado
# from producto import Producto

class Inventario:
    """
    Clase que gestiona la colección de productos, con persistencia en archivos.
    """
    def __init__(self, archivo_inventario="inventario.txt"):
        """
        Constructor de la clase Inventario.
        Inicializa el diccionario de productos y carga los datos desde el archivo.
        """
        self.productos = {}  # Clave: ID del producto, Valor: Objeto Producto
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()

    def _guardar_inventario(self):
        """
        Método privado para guardar el estado actual del inventario en el archivo.
        Maneja excepciones de escritura.
        """
        try:
            with open(self.archivo_inventario, 'w') as f:
                for producto in self.productos.values():
                    f.write(producto.to_csv_line())
            print(f"El inventario se ha guardado exitosamente en '{self.archivo_inventario}'.")
            return True
        except PermissionError:
            print(f"Error: No se tienen permisos para escribir en el archivo '{self.archivo_inventario}'.")
            return False
        except Exception as e:
            print(f"Error inesperado al guardar el archivo: {e}")
            return False

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo al inicio del programa.
        Maneja excepciones si el archivo no existe o está corrupto.
        """
        try:
            with open(self.archivo_inventario, 'r') as f:
                for linea in f:
                    partes = linea.strip().split(',')
                    if len(partes) == 4:
                        try:
                            id_prod, nombre, cantidad, precio = partes
                            cantidad = int(cantidad)
                            precio = float(precio)
                            producto = Producto(id_prod, nombre, cantidad, precio)
                            self.productos[id_prod] = producto
                        except (ValueError, IndexError):
                            print(f"Advertencia: Línea con formato incorrecto encontrada y omitida: '{linea.strip()}'")
                            continue
            print("Inventario cargado exitosamente desde el archivo.")
        except FileNotFoundError:
            print("El archivo de inventario no se encontró. Se creará uno nuevo al guardar.")
        except PermissionError:
            print(f"Error: No se tienen permisos para leer el archivo '{self.archivo_inventario}'.")
        except Exception as e:
            print(f"Error inesperado al cargar el archivo: {e}")

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario y lo guarda en el archivo.
        """
        if producto.get_id() in self.productos:
            print(f"Error: El producto con ID '{producto.get_id()}' ya existe.")
            return False
        else:
            self.productos[producto.get_id()] = producto
            if self._guardar_inventario():
                print(f"Producto '{producto.get_nombre()}' añadido exitosamente.")
                return True
            else:
                # Si falla el guardado, se revierte la adición para mantener la consistencia
                del self.productos[producto.get_id()]
                return False

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID y guarda el cambio.
        """
        if id_producto in self.productos:
            nombre_producto = self.productos[id_producto].get_nombre()
            del self.productos[id_producto]
            if self._guardar_inventario():
                print(f"Producto '{nombre_producto}' eliminado exitosamente.")
                return True
            else:
                return False
        else:
            print(f"Error: No se encontró un producto con ID '{id_producto}'.")
            return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza la cantidad o el precio de un producto y guarda el cambio.
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            cambio_realizado = False
            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)
                print(f"Cantidad de '{producto.get_nombre()}' actualizada a {nueva_cantidad}.")
                cambio_realizado = True
            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)
                print(f"Precio de '{producto.get_nombre()}' actualizado a ${nuevo_precio:.2f}.")
                cambio_realizado = True

            if cambio_realizado:
                if self._guardar_inventario():
                    return True
                else:
                    return False
            else:
                print("No se realizaron cambios en el producto.")
                return False
        else:
            print(f"Error: No se encontró un producto con ID '{id_producto}'.")
            return False

    def buscar_producto_por_id(self, id_producto):
        """
        Busca un producto por su ID y lo retorna.
        """
        return self.productos.get(id_producto)

    def buscar_productos_por_nombre(self, nombre_buscado):
        """
        Busca productos por nombre (búsqueda parcial e insensible a mayúsculas/minúsculas).
        Retorna una lista de productos que coinciden.
        """
        resultados = []
        for producto in self.productos.values():
            if nombre_buscado.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos_los_productos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- Inventario Actual ---")
            for producto in self.productos.values():
                print(producto)
            print("-------------------------")

# Archivo: main.py

def menu_principal():
    """
    Función que implementa la interfaz de usuario en la consola.
    Permite al usuario interactuar con el inventario.
    """
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        print("--------------------------------------")

        opcion = input("Por favor, seleccione una opción (1-6): ")

        if opcion == '1':
            print("\n--- Agregar Nuevo Producto ---")
            id_prod = input("Ingrese el ID del producto: ").strip()
            nombre_prod = input("Ingrese el nombre del producto: ").strip()
            try:
                cantidad_prod = int(input("Ingrese la cantidad: "))
                precio_prod = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_prod, nombre_prod, cantidad_prod, precio_prod)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Error: Cantidad o precio inválidos. Por favor, ingrese números.")

        elif opcion == '2':
            print("\n--- Eliminar Producto ---")
            id_eliminar = input("Ingrese el ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_eliminar)

        elif opcion == '3':
            print("\n--- Actualizar Producto ---")
            id_actualizar = input("Ingrese el ID del producto a actualizar: ").strip()
            if inventario.buscar_producto_por_id(id_actualizar):
                try:
                    nueva_cantidad_str = input("Ingrese la nueva cantidad (deje vacío para no cambiar): ").strip()
                    nuevo_precio_str = input("Ingrese el nuevo precio (deje vacío para no cambiar): ").strip()

                    nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
                    nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None

                    inventario.actualizar_producto(id_actualizar, nueva_cantidad, nuevo_precio)
                except ValueError:
                    print("Error: La cantidad o el precio ingresado no es válido.")
            else:
                print(f"Error: No se encontró un producto con ID '{id_actualizar}'.")

        elif opcion == '4':
            print("\n--- Buscar Producto por Nombre ---")
            nombre_buscar = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
            resultados = inventario.buscar_productos_por_nombre(nombre_buscar)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} producto(s) con nombres similares:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_todos_los_productos()

        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()