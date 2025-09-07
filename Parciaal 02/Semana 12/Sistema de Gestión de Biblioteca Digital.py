# Definimos la clase Libro
class Libro:
    """
    Representa un libro en la biblioteca.
    Los atributos inmutables (título y autor) se almacenan en una tupla.
    """

    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Usamos una tupla para el título y el autor, ya que son inmutables
        self.info_basica = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        # Atributo para controlar el estado de préstamo del libro
        self.prestado = False

    def __str__(self):
        """
        Método de cadena para una representación legible del objeto Libro.
        """
        return f"'{self.info_basica[0]}' por {self.info_basica[1]} (ISBN: {self.isbn})"


# Definimos la clase Usuario
class Usuario:
    """
    Representa a un usuario de la biblioteca.
    Cada usuario tiene un ID único y una lista de los libros que ha tomado prestados.
    """

    def __init__(self, nombre: str, id_usuario: int):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar los objetos Libro prestados

    def __str__(self):
        """
        Método de cadena para una representación legible del objeto Usuario.
        """
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Definimos la clase principal: Biblioteca
class Biblioteca:
    """
    Clase principal que gestiona las colecciones de libros, usuarios y préstamos.
    Utiliza un diccionario para libros (acceso por ISBN) y un conjunto para usuarios (IDs únicos).
    """

    def __init__(self):
        # Diccionario para almacenar libros. La clave es el ISBN para una búsqueda eficiente.
        self.libros_disponibles = {}
        # Conjunto para asegurar IDs de usuario únicos.
        self.usuarios_registrados_ids = set()
        # Diccionario para mapear IDs de usuario a objetos Usuario.
        self.usuarios_registrados_obj = {}

    # --- Métodos de Gestión de Libros ---

    def anadir_libro(self, libro: Libro):
        """Añade un libro a la colección de la biblioteca."""
        if libro.isbn in self.libros_disponibles:
            print(f"Error: El libro con ISBN {libro.isbn} ya existe en la biblioteca.")
        else:
            self.libros_disponibles[libro.isbn] = libro
            print(f"'{libro.info_basica[0]}' añadido a la biblioteca con éxito.")

    def quitar_libro(self, isbn: str):
        """Quita un libro de la biblioteca usando su ISBN."""
        if isbn not in self.libros_disponibles:
            print(f"Error: No se encontró el libro con ISBN {isbn}.")
        else:
            libro = self.libros_disponibles[isbn]
            if libro.prestado:
                print(f"Error: No se puede quitar el libro '{libro.info_basica[0]}' porque está prestado.")
            else:
                del self.libros_disponibles[isbn]
                print(f"'{libro.info_basica[0]}' eliminado de la biblioteca.")

    # --- Métodos de Gestión de Usuarios ---

    def registrar_usuario(self, usuario: Usuario):
        """Registra un nuevo usuario en la biblioteca."""
        if usuario.id_usuario in self.usuarios_registrados_ids:
            print(f"Error: El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios_registrados_ids.add(usuario.id_usuario)
            self.usuarios_registrados_obj[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def dar_de_baja_usuario(self, id_usuario: int):
        """Da de baja a un usuario de la biblioteca."""
        if id_usuario not in self.usuarios_registrados_ids:
            print(f"Error: El usuario con ID {id_usuario} no está registrado.")
        else:
            usuario = self.usuarios_registrados_obj[id_usuario]
            if usuario.libros_prestados:
                print(f"Error: No se puede dar de baja a '{usuario.nombre}' porque tiene libros prestados.")
            else:
                self.usuarios_registrados_ids.remove(id_usuario)
                del self.usuarios_registrados_obj[id_usuario]
                print(f"Usuario '{usuario.nombre}' dado de baja con éxito.")

    # --- Métodos de Préstamo y Devolución ---

    def prestar_libro(self, isbn: str, id_usuario: int):
        """Presta un libro a un usuario si está disponible."""
        if id_usuario not in self.usuarios_registrados_ids:
            print(f"Error: Usuario con ID {id_usuario} no está registrado.")
            return

        if isbn not in self.libros_disponibles:
            print(f"Error: El libro con ISBN {isbn} no existe en la biblioteca.")
            return

        libro = self.libros_disponibles[isbn]
        if libro.prestado:
            print(f"Error: '{libro.info_basica[0]}' ya está prestado.")
        else:
            libro.prestado = True
            usuario = self.usuarios_registrados_obj[id_usuario]
            usuario.libros_prestados.append(libro)
            print(f"'{libro.info_basica[0]}' prestado a {usuario.nombre}.")

    def devolver_libro(self, isbn: str, id_usuario: int):
        """Permite a un usuario devolver un libro."""
        if id_usuario not in self.usuarios_registrados_ids:
            print(f"Error: Usuario con ID {id_usuario} no está registrado.")
            return

        if isbn not in self.libros_disponibles:
            print(f"Error: El libro con ISBN {isbn} no existe en la biblioteca.")
            return

        libro = self.libros_disponibles[isbn]
        usuario = self.usuarios_registrados_obj[id_usuario]

        if libro not in usuario.libros_prestados:
            print(f"Error: '{libro.info_basica[0]}' no estaba prestado a {usuario.nombre}.")
        else:
            libro.prestado = False
            usuario.libros_prestados.remove(libro)
            print(f"'{libro.info_basica[0]}' devuelto por {usuario.nombre}.")

    # --- Métodos de Búsqueda y Listado ---

    def buscar_libros(self, criterio: str, valor: str):
        """
        Busca libros por título, autor o categoría.
        El criterio debe ser 'titulo', 'autor' o 'categoria'. La búsqueda no es sensible a mayúsculas.
        """
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and libro.info_basica[0].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == "autor" and libro.info_basica[1].lower() == valor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and libro.categoria.lower() == valor.lower():
                resultados.append(libro)

        if resultados:
            print(f"\nResultados de la búsqueda por {criterio} '{valor}':")
            for libro in resultados:
                print(f"  - {libro}")
        else:
            print(f"\nNo se encontraron libros con {criterio} '{valor}'.")
        return resultados

    def listar_libros_prestados_a_usuario(self, id_usuario: int):
        """Muestra los libros que un usuario tiene actualmente prestados."""
        if id_usuario not in self.usuarios_registrados_ids:
            print(f"Error: Usuario con ID {id_usuario} no está registrado.")
            return

        usuario = self.usuarios_registrados_obj[id_usuario]
        if not usuario.libros_prestados:
            print(f"\n{usuario.nombre} no tiene libros prestados en este momento.")
        else:
            print(f"\nLibros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(f"  - {libro}")


# --- Bloque de Pruebas ---
if __name__ == "__main__":
    # 1. Inicializar la biblioteca y crear objetos de prueba
    mi_biblioteca = Biblioteca()

    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo Mágico", "978-3-16-148410-0")
    libro2 = Libro("El señor de los anillos", "J.R.R. Tolkien", "Fantasía", "978-0-618-05856-4")
    libro3 = Libro("1984", "George Orwell", "Distopía", "978-0-452-28423-4")

    usuario1 = Usuario("Ana Pérez", 101)
    usuario2 = Usuario("Luis Gómez", 102)

    print("--- 1. Añadiendo libros y registrando usuarios ---")
    mi_biblioteca.anadir_libro(libro1)
    mi_biblioteca.anadir_libro(libro2)
    mi_biblioteca.anadir_libro(libro3)

    mi_biblioteca.registrar_usuario(usuario1)
    mi_biblioteca.registrar_usuario(usuario2)
    mi_biblioteca.registrar_usuario(usuario2)  # Intento de registrar un usuario ya existente

    print("\n--- 2. Probando la funcionalidad de préstamo y devolución ---")
    mi_biblioteca.prestar_libro(libro1.isbn, usuario1.id_usuario)
    mi_biblioteca.prestar_libro(libro1.isbn, usuario2.id_usuario)  # Intento de prestar un libro que ya está prestado
    mi_biblioteca.prestar_libro(libro2.isbn, usuario2.id_usuario)

    mi_biblioteca.listar_libros_prestados_a_usuario(usuario1.id_usuario)
    mi_biblioteca.listar_libros_prestados_a_usuario(usuario2.id_usuario)

    print("\n--- 3. Devolviendo un libro ---")
    mi_biblioteca.devolver_libro(libro1.isbn, usuario1.id_usuario)
    mi_biblioteca.listar_libros_prestados_a_usuario(usuario1.id_usuario)

    print("\n--- 4. Buscando libros ---")
    mi_biblioteca.buscar_libros("autor", "J.R.R. Tolkien")
    mi_biblioteca.buscar_libros("categoria", "Distopía")
    mi_biblioteca.buscar_libros("titulo", "El señor de los anillos")

    print("\n--- 5. Quitando libros y usuarios ---")
    mi_biblioteca.quitar_libro(libro3.isbn)
    mi_biblioteca.quitar_libro(libro1.isbn)  # No se puede quitar, está prestado
    mi_biblioteca.devolver_libro(libro1.isbn, usuario1.id_usuario)
    mi_biblioteca.quitar_libro(libro1.isbn)  # Ahora sí se puede

    mi_biblioteca.dar_de_baja_usuario(usuario2.id_usuario)
    mi_biblioteca.dar_de_baja_usuario(usuario1.id_usuario)  # No se puede dar de baja, tiene un libro prestado