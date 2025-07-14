# Clase que representa un archivo de registro
class LogFile:
    def __init__(self, filename):
        # Constructor: se ejecuta automáticamente al crear una instancia
        self.filename = filename
        self.file = open(self.filename, 'w')  # Abrimos el archivo para escribir
        print(f"[INFO] Archivo '{self.filename}' abierto.")

    def write_log(self, message):
        # Método para escribir un mensaje en el archivo
        self.file.write(message + '\n')
        print(f"[LOG] Mensaje escrito: {message}")

    def __del__(self):
        # Destructor: se ejecuta automáticamente cuando el objeto es destruido
        if self.file:
            self.file.close()
            print(f"[INFO] Archivo '{self.filename}' cerrado.")


# Clase que representa a un usuario
class Usuario:
    def __init__(self, nombre, edad):
        # Constructor: inicializa los atributos del usuario
        self.nombre = nombre
        self.edad = edad
        print(f"[CREADO] Usuario {self.nombre}, Edad: {self.edad}")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre} | Edad: {self.edad}")

    def __del__(self):
        # Destructor: mensaje al eliminar al usuario
        print(f"[BORRADO] Usuario {self.nombre} ha sido eliminado.")


# Ejecución principal del programa
if __name__ == "__main__":
    # Creamos un objeto de tipo LogFile
    log = LogFile("registro.txt")
    log.write_log("Programa iniciado")

    # Creamos usuarios
    usuario1 = Usuario("Ana", 25)
    usuario1.mostrar_info()

    usuario2 = Usuario("Carlos", 30)
    usuario2.mostrar_info()

    log.write_log("Usuarios creados y mostrados")

    # Eliminamos manualmente los objetos (opcional, para forzar el destructor)
    del usuario1
    del usuario2
    del log

    print("[FIN DEL PROGRAMA]")
