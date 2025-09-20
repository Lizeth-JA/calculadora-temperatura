def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Soy el colaborador 1: Añadir Kelvin a Celsius
def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

# Colaborador 2: Añadir Celsius a Kelvin
def celsius_a_kelvin(celsius):
    return celsius + 273.15

# Colaborador 3: Añadir Fahrenheit a Kelvin
def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

if __name__ == "__main__":
    temp_c = float(input("Introduce la temperatura en Celsius: "))
    print(f"{temp_c}°C es {celsius_a_fahrenheit(temp_c)}°F")
    print(f"{temp_c}°C es {celsius_a_kelvin(temp_c)}K")

    temp_f = float(input("Introduce la temperatura en Fahrenheit: "))
    print(f"{temp_f}°F es {fahrenheit_a_celsius(temp_f)}°C")
    print(f"{temp_f}°F es {fahrenheit_a_kelvin(temp_f)}K")

    temp_k = float(input("Introduce la temperatura en Kelvin: "))
    print(f"{temp_k}K es {kelvin_a_celsius(temp_k)}°C")
