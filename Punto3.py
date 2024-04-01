def contar_vocales_consonantes(letras):
    """
    Función para contar cuántas vocales y consonantes hay en una lista de letras.
    
    Args:
    letras (list): Lista de letras
    
    Returns:
    int: Número de vocales
    int: Número de consonantes
    """
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0
    
    for letra in letras:
        if letra.isalpha():
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
    
    return num_vocales, num_consonantes

def main():
    try:
        letras = []
        for i in range(10):
            letra = input(f"Ingrese la letra {i+1}: ")
            letras.append(letra)

        num_vocales, num_consonantes = contar_vocales_consonantes(letras)

        print(f"Se ingresaron {num_vocales} vocales y {num_consonantes} consonantes.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")

if __name__ == "__main__":
    main()
