def calcular_promedio_edad_por_genero(estudiantes):
    """
    Función para calcular el promedio de edad de hombres y mujeres en un grupo de estudiantes.
    
    Args:
    estudiantes (list): Lista de tuplas (edad, género) de cada estudiante.
    
    Returns:
    float: Promedio de edad de hombres.
    float: Promedio de edad de mujeres.
    """
    total_edad_hombres = 0
    total_edad_mujeres = 0
    num_hombres = 0
    num_mujeres = 0
    
    for edad, genero in estudiantes:
        if genero.lower() == 'hombre':
            total_edad_hombres += edad
            num_hombres += 1
        elif genero.lower() == 'mujer':
            total_edad_mujeres += edad
            num_mujeres += 1
    
    promedio_edad_hombres = total_edad_hombres / num_hombres if num_hombres > 0 else 0
    promedio_edad_mujeres = total_edad_mujeres / num_mujeres if num_mujeres > 0 else 0
    
    return promedio_edad_hombres, promedio_edad_mujeres

def main():
    try:
        num_estudiantes = int(input("Ingrese el número de estudiantes: "))
        estudiantes = []
        
        for i in range(num_estudiantes):
            edad = int(input(f"Ingrese la edad del estudiante {i+1}: "))
            genero = input(f"Ingrese el género del estudiante {i+1} (Hombre/Mujer): ")
            estudiantes.append((edad, genero))
        
        promedio_hombres, promedio_mujeres = calcular_promedio_edad_por_genero(estudiantes)
        
        print(f"Promedio de edad de hombres: {promedio_hombres:.2f}")
        print(f"Promedio de edad de mujeres: {promedio_mujeres:.2f}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para la edad.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
