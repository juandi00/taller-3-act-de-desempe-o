def calcular_costo_anual(costo_mensual):
    """
    Función para calcular el costo anual de los servicios públicos.
    
    Args:
    costo_mensual (float): Costo mensual de los servicios públicos.
    
    Returns:
    float: Costo anual de los servicios públicos.
    """
    return costo_mensual * 12

def calcular_costo_mensual(costo_anual):
    """
    Función para calcular el costo mensual de los servicios públicos.
    
    Args:
    costo_anual (float): Costo anual de los servicios públicos.
    
    Returns:
    float: Costo mensual de los servicios públicos.
    """
    return costo_anual / 12

def main():
    try:
        costo_mensual = float(input("Ingrese el costo mensual de los servicios públicos: "))
        
        costo_anual = calcular_costo_anual(costo_mensual)
        costo_mensual_individual = calcular_costo_mensual(costo_anual)
        
        print(f"El costo anual de los servicios públicos es: {costo_anual:.2f}")
        print(f"El costo mensual de los servicios públicos es: {costo_mensual_individual:.2f}")
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el costo mensual.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
