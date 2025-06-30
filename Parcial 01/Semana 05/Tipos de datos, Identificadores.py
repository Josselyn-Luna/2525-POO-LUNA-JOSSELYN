# Programa que calcula el área de un círculo a partir del radio ingresado
# Usa float, string, boolean e int, e incluye comentarios para explicar cada parte

import math  # Librería para usar el valor de pi

def calcular_area_circulo(radio):
    """Calcula el área de un círculo con fórmula: A = π * r²"""
    area = math.pi * radio ** 2
    return area

# Ingreso de datos
radio_ingresado = input("Ingrese el radio del círculo (en cm): ")

try:
    # Conversión a float
    radio = float(radio_ingresado)

    # Validar que el radio sea positivo
    if radio <= 0:
        print("El radio debe ser mayor a cero.")
    else:
        # Cálculo del área
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} cm es: {area:.2f} cm²")

except ValueError:
    print("Por favor, ingrese un número válido.")
