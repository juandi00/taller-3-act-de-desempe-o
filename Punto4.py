def escrutinio_votos(votos):
    """
    Función para realizar el escrutinio de votos y determinar al ganador por mayoría simple.
    
    Args:
    votos (list): Lista de votos para los candidatos
    
    Returns:
    str: El nombre del candidato ganador, o "Empate" si hay un empate en votos.
    """
    votos_candidato1 = votos.count(1)
    votos_candidato2 = votos.count(2)
    votos_candidato3 = votos.count(3)
    
    max_votos = max(votos_candidato1, votos_candidato2, votos_candidato3)
    
    if max_votos == votos_candidato1:
        return "Candidato 1"
    elif max_votos == votos_candidato2:
        return "Candidato 2"
    elif max_votos == votos_candidato3:
        return "Candidato 3"
    else:
        return "Empate"

def main():
    votos = []
    for i in range(200):
        voto = int(input(f"Ingrese el voto del elector {i+1} (1 para Candidato 1, 2 para Candidato 2, 3 para Candidato 3): "))
        while voto not in [1, 2, 3]:
            print("Voto inválido. Por favor ingrese 1, 2 o 3.")
            voto = int(input(f"Ingrese el voto del elector {i+1} (1 para Candidato 1, 2 para Candidato 2, 3 para Candidato 3): "))
        votos.append(voto)
    
    ganador = escrutinio_votos(votos)
    
    print(f"\nEl ganador de las elecciones es: {ganador}")

if __name__ == "__main__":
    main()
