def calcular_sueldo_promedio(sueldos):
    """
    Función para calcular el sueldo promedio de un grupo de empleados.
    
    Args:
    sueldos (list): Lista de sueldos de los empleados
    
    Returns:
    float: Sueldo promedio
    """
    if not sueldos:
        return None  # Si la lista de sueldos está vacía, retorna None
    
    total_sueldos = sum(sueldos)
    sueldo_promedio = total_sueldos / len(sueldos)
    return sueldo_promedio

def main():
    try:
        cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))
        sueldos = []

        for i in range(cantidad_empleados):
            sueldo = float(input(f"Ingrese el sueldo del empleado {i+1}: "))
            sueldos.append(sueldo)

        sueldo_promedio = calcular_sueldo_promedio(sueldos)

        if sueldo_promedio is not None:
            print(f"El sueldo promedio del grupo de {cantidad_empleados} empleados es: ${sueldo_promedio:.2f}")
        else:
            print("No se ingresaron sueldos.")
    except ValueError:
        print("Error: Ingrese un número válido para la cantidad de empleados o para los sueldos.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
