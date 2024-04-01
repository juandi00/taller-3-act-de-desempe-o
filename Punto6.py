def calcular_precio_actualizado(precio_anterior, inflaciones):
    """
    Función para calcular el precio actualizado de una planta basado en los valores de inflación.
    
    Args:
    precio_anterior (float): Precio anterior de la planta.
    inflaciones (list): Lista de valores de inflación mensual de los últimos seis meses.
    
    Returns:
    float: Precio actualizado de la planta.
    """
    factor_inflacion_acumulado = 1.0
    for inflacion in inflaciones:
        factor_inflacion_acumulado *= (1 + inflacion)
    precio_actualizado = precio_anterior * factor_inflacion_acumulado
    return precio_actualizado

def main():
    try:
        precio_anterior = float(input("Ingrese el precio anterior de la planta: "))
        inflaciones = []
        for i in range(6):
            inflacion = float(input(f"Ingrese la inflación del mes {i+1} (en decimal): "))
            inflaciones.append(inflacion)
        
        precio_actualizado = calcular_precio_actualizado(precio_anterior, inflaciones)
        
        print(f"El precio actualizado de la planta es: {precio_actualizado:.2f}")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para el precio anterior y las inflaciones.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
