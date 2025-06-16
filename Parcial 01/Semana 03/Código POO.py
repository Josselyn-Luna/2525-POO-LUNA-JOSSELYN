# Ejemplo: Gestión de información diaria del clima
#Diseña una solución utilizando el paradigma de POO.
#Crea una clase que represente la información diaria del clima.
class DailyWeather:
    """
    Clase: representa la información del clima de un día específico.
    Encapsula la temperatura mínima, máxima y la condición general.
    """
    def __init__(self, date="Desconocida", min_temp=0, max_temp=0, condition="N/A"):
        # Atributos que describen el clima diario
        self.date = date
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.condition = condition # Ej: "Día soleado", "Día lluvioso", "Día nublado"

    def set_temperatures(self, min_t, max_t):
        """
        Establece la temperatura mínima y máxima
        """
        self.min_temp = min_t
        self.max_temp = max_t
        print(f"Temperaturas actualizadas para {self.date}: Mín {self.min_temp}°C, Máx {self.max_temp}°C.")

    def set_condition(self, new_condition):
        """
        Establece la condición climática.
        """
        self.condition = new_condition
        print(f"Condición actualizada para {self.date}: {self.condition}.")

    def get_average_daily_temp(self):
        """
        Calcula y retorna la temperatura promedio del día.
        """
        if self.min_temp is not None and self.max_temp is not None:
            return (self.min_temp + self.max_temp) / 2
        return 0 # Retorna 0 si las temperaturas no están definidas

    def display_info(self):
        """
        Muestra toda la información del clima para este día.
        """
        avg_temp = self.get_average_daily_temp()
        print(f"--- Clima del día: {self.date} ---")
        print(f"  Temperatura Mínima: {self.min_temp}°C")
        print(f"  Temperatura Máxima: {self.max_temp}°C")
        print(f"  Condición: {self.condition}")
        print(f"  Temperatura Promedio: {avg_temp:.2f}°C")

# --- Uso de la clase DailyWeather ---

# Crear una instancia de la clase DailyWeather para hoy
today_weather = DailyWeather(date="2025-06-13")

# Usar los métodos para establecer la información del clima
today_weather.set_temperatures(min_t=17, max_t=30)
today_weather.set_condition(new_condition="Soleado con pocas nubes")

# Mostrar la información del clima para hoy
today_weather.display_info()

print("\n--- Ejemplo con otro día ---")
yesterday_weather = DailyWeather("2025-06-14", 16, 18, "Día lluvioso")
yesterday_weather.display_info()

# Acceder a un atributo directamente
print(f"\nLa temperatura mínima de ayer fue: {yesterday_weather.min_temp}°C")