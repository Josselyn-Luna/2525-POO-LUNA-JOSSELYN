# Ejemplo: Gestión de temperaturas diarias y cálculo del promedio semanal

#Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal.


temperatures = []


# Función para ingresar la temperatura de un día
def record_daily_temperature(temperature):
    global temperatures
    temperatures.append(temperature)
    print(f"Temperatura {temperature}°C registrada.")


# Función para calcular el promedio semanal de las temperaturas
def calculate_weekly_average():
    global temperatures
    if not temperatures:  # Verificamos si la lista está vacía para evitar división por cero
        return 0

    total_temperature = sum(temperatures)
    average = total_temperature / len(temperatures)
    return average

# Uso de las funciones en la programación tradicional para el ejemplo de temperaturas

# Entrada de datos diarios (temperaturas)
record_daily_temperature(28) # (Lunes)
record_daily_temperature(25) # (Martes)
record_daily_temperature(20) # (Miércoles)
record_daily_temperature(23) # (Jueves)
record_daily_temperature(28) # (Viernes)
record_daily_temperature(25) # (Sábado)
record_daily_temperature(24) # (Domingo)

# Calcular el promedio semanal
weekly_average = calculate_weekly_average()

# Imprimir el promedio semanal final
print("\nTemperaturas de esta semana:", temperatures)
print("El promedio de las temperaturas de esta semana es: ", weekly_average,"°C")