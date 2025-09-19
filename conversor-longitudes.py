def metros_a_kilometros(metros):
    return metros / 1000

def kilometros_a_metros(km):
    return km * 1000

def metros_a_centimetros(metros):
    return metros * 100

def centimetros_a_metros(cm):
    return cm / 100

def pulgadas_a_centimetros(inch):
    return inch * 2.54

def centimetros_a_pulgadas(cm):
    return cm / 2.54


# Menu
if __name__ == "__main__":
    while True:
        print("\n Conversor de Unidades de Longitud")
        print("1. Metros → Kilómetros")
        print("2. Kilómetros → Metros")
        print("3. Metros → Centímetros")
        print("4. Centímetros → Metros")
        print("5. Pulgadas → Centímetros")
        print("6. Centímetros → Pulgadas")
        print("7. Salir")

        opcion = input("Elige una opción (1-7): ")

        if opcion == "7":
            print("¡BYE! ")
            break

        valor = float(input("Ingresa el valor a convertir: "))

        if opcion == "1":
            print(f"{valor} m = {metros_a_kilometros(valor)} km")
        elif opcion == "2":
            print(f"{valor} km = {kilometros_a_metros(valor)} m")
        elif opcion == "3":
            print(f"{valor} m = {metros_a_centimetros(valor)} cm")
        elif opcion == "4":
            print(f"{valor} cm = {centimetros_a_metros(valor)} m")
        elif opcion == "5":
            print(f"{valor} in = {pulgadas_a_centimetros(valor)} cm")
        elif opcion == "6":
            print(f"{valor} cm = {centimetros_a_pulgadas(valor)} in")
        else:
            print("Opción inválida")
