def calcular_salario_empleados(salarios):
    """
    Calcula el salario promedio de los empleados y el salario de cada uno con un incremento del 2.5%.
    
    Args:
    salarios (list): Lista de salarios mensuales de los empleados.
    
    Returns:
    float: Salario promedio de los empleados.
    list: Lista de salarios actualizados con un incremento del 2.5%.
    """
    total_salarios = sum(salarios)
    promedio_salarios = total_salarios / len(salarios)
    salarios_actualizados = [salario * 1.025 for salario in salarios]  # Incremento del 2.5%
    return promedio_salarios, salarios_actualizados

def main():
    try:
        salarios = []
        for i in range(1, 21):
            salario = float(input(f"Ingrese el salario del empleado {i}: "))
            salarios.append(salario)

        promedio_salarios, salarios_actualizados = calcular_salario_empleados(salarios)

        print(f"\nEl salario promedio de los empleados es: ${promedio_salarios:.2f}")

        print("\nSalarios de los empleados con un incremento del 2.5%:")
        for i, salario_actualizado in enumerate(salarios_actualizados, start=1):
            print(f"Empleado {i}: ${salario_actualizado:.2f}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para los salarios.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
