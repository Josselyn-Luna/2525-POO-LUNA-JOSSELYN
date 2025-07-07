# Programa: Sistema de Zoológico utilizando POO

# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre     # Atributo encapsulado
        self._edad = edad         # Atributo encapsulado

    def hacer_sonido(self):
        return "Este animal hace un sonido genérico."

    def get_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad} años"

    # Métodos de acceso (getters)
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    # Métodos de modificación (setters)
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            print("Edad no válida.")

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescribimos el método (polimorfismo)
    def hacer_sonido(self):
        return "Guau guau!"

    def get_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad} años, Raza: {self.raza}"

# Otra clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Polimorfismo: método sobrescrito
    def hacer_sonido(self):
        return "Miau~"

    def get_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad} años, Color: {self.color}"

# Programa principal
if __name__ == "__main__":
    # Instancias
    perro1 = Perro("Firulais", 4, "Labrador")
    gato1 = Gato("Mishi", 2, "Negro")

    # Mostramos información
    print(perro1.get_info())
    print(perro1.hacer_sonido())  # Polimorfismo

    print(gato1.get_info())
    print(gato1.hacer_sonido())  # Polimorfismo

    # Encapsulación: modificamos valores con métodos
    perro1.set_edad(5)
    print(f"Edad actualizada del perro: {perro1.get_edad()} años")
