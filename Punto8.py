import random

class BingoDigital:
    def __init__(self):
        self.carton = self.generar_carton()
        self.numeros_extraidos = set()

    def generar_carton(self):
        return [[random.randint(1, 15) for _ in range(5)] for _ in range(5)]

    def mostrar_carton(self):
        print("=== Cartón de Bingo ===")
        for fila in self.carton:
            print(fila)

    def extraer_numero(self):
        numero = random.randint(1, 15)
        self.numeros_extraidos.add(numero)
        print(f"Número extraído: {numero}")
        self.mostrar_carton()

    def verificar_ganador(self):
        for fila in self.carton:
            if all(numero in self.numeros_extraidos for numero in fila):
                return True
        for columna in range(5):
            if all(self.carton[fila][columna] in self.numeros_extraidos for fila in range(5)):
                return True
        if all(self.carton[i][i] in self.numeros_extraidos for i in range(5)):
            return True
        if all(self.carton[i][4-i] in self.numeros_extraidos for i in range(5)):
            return True
        return False

def main():
    bingo = BingoDigital()
    bingo.mostrar_carton()
    
    while True:
        continuar = input("¿Desea extraer un número? (s/n): ").lower()
        if continuar != 's':
            break
        bingo.extraer_numero()
        if bingo.verificar_ganador():
            print("¡Bingo! ¡Ha ganado!")
            break
    print("Fin del juego.")

if __name__ == "__main__":
    main()
