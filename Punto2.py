def calcular_potencia_de_dos_hasta_mil(x):
    """
    Función para calcular la potencia de 2 de un número x hasta alcanzar o superar 1000.
    
    Args:
    x (int): Número base
    
    Returns:
    list: Lista de potencias de 2 hasta alcanzar o superar 1000
    """
    potencias = []
    potencia = 1
    while potencia <= 1000:
        potencias.append(potencia)
        potencia *= 2
    return potencias

def main():
    try:
        x = int(input("Ingrese un número para calcular sus potencias de 2 hasta 1000: "))
        potencias = calcular_potencia_de_dos_hasta_mil(x)
        print(f"Potencias de 2 de {x} hasta alcanzar o superar 1000:")
        for potencia in potencias:
            print(potencia)
    except ValueError:
        print("Error: Ingrese un número entero válido.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
