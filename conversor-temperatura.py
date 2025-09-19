def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def fahrenheit_a_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_a_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def menu():
    print("\n Conversor de Temperaturas")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")
    print("7. Salir")

    opcion = input("Elige una opción (1-7): ")

    if opcion == "7":
        print("¡BYE!")
        return 

    try:
        valor = float(input("Introduce la temperatura: "))
    except ValueError:
        print("Ingresa un número válido")
        return menu()

    if opcion == "1":
        print(f"{valor} °C = {celsius_a_fahrenheit(valor)} °F")
    elif opcion == "2":
        print(f"{valor} °F = {fahrenheit_a_celsius(valor)} °C")
    elif opcion == "3":
        print(f"{valor} °C = {celsius_a_kelvin(valor)} K")
    elif opcion == "4":
        print(f"{valor} K = {kelvin_a_celsius(valor)} °C")
    elif opcion == "5":
        print(f"{valor} °F = {fahrenheit_a_kelvin(valor)} K")
    elif opcion == "6":
        print(f"{valor} K = {kelvin_a_fahrenheit(valor)} °F")
    else:
        print("Opción inválida")

    return menu()

if __name__ == "__main__":
    menu()
