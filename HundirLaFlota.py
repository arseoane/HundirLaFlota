# ==========================================
# PARTE 1: LOGICA ESTRUCTURADA (REPASO)
# ==========================================

def esNavio(valor):
    return valor > 0


def queNavioEs(valor):
    naves = {1: "Submarino", 2: "Buque", 4: "Portaaviones"}
    return naves.get(valor, "Desconocido")


def salidaPorPantalla(coord_x, coord_y, nombre):
    print(f"   [Estructurado] Detectado {nombre} en ({coord_x}, {coord_y})")


def recorrerFila(fila, index_fila):
    partes = 0
    for index_col, valor in enumerate(fila):
        if esNavio(valor):
            nombre = queNavioEs(valor)
            salidaPorPantalla(index_fila, index_col, nombre)
            partes += 1
    return partes


def recorrerTablero(tablero):
    total = 0
    for i, fila in enumerate(tablero):
        total += recorrerFila(fila, i)
    return total


# ==========================================
# PARTE 2: PROGRAMACIÓN ORIENTADA A OBJETOS
# ==========================================

class Nave:
    """Representa un barco con su estado de salud."""

    def __init__(self, nombre, tamano):
        self.nombre = nombre
        self.tamano = tamano
        self.vida = tamano

    def recibir_disparo(self):
        self.vida -= 1
        return "Hundido" if self.vida <= 0 else "Tocado"


class Tablero:
    """Gestiona la cuadrícula y la ubicación de los objetos Nave."""

    def __init__(self, tamano=10):
        self.tamano = tamano
        self.matriz = [[None for _ in range(tamano)] for _ in range(tamano)]

    def colocar_nave(self, nave, x, y, orientacion):
        # Lógica para ocupar celdas con la misma instancia de Nave
        for i in range(nave.tamano):
            if orientacion.upper() == "H":
                self.matriz[x][y + i] = nave
            else:
                self.matriz[x + i][y] = nave

    def comprobar_impacto(self, x, y):
        # Validar si las coordenadas están dentro del tablero
        if not (0 <= x < self.tamano and 0 <= y < self.tamano):
            return "Fuera de rango"

        objetivo = self.matriz[x][y]
        if objetivo is None:
            return "Agua"

        # Si hay impacto, se llama al método de la clase Nave
        resultado_estado = objetivo.recibir_disparo()
        return (resultado_estado, objetivo.nombre)


class Juego:
    """Controlador principal que orquestra el flujo."""

    def __init__(self):
        self.tablero = Tablero(10)
        self.inicializar_naves()

    def inicializar_naves(self):
        # Instanciamos los objetos
        submarino = Nave("Submarino", 1)
        buque = Nave("Buque", 2)
        portaaviones = Nave("Portaaviones", 4)

        # Los posicionamos en el tablero
        self.tablero.colocar_nave(submarino, 0, 0, "H")
        self.tablero.colocar_nave(buque, 5, 3, "V")
        self.tablero.colocar_nave(portaaviones, 2, 2, "H")

    def lanzar_ataque(self, x, y):
        print(f"\n--- Disparo en ({x}, {y}) ---")
        resultado = self.tablero.comprobar_impacto(x, y)
        self.mostrar_resultado(resultado)

    def mostrar_resultado(self, resultado):
        if resultado == "Agua":
            print("Resultado: ¡Agua!")
        elif resultado == "Fuera de rango":
            print("Error: Coordenadas inválidas.")
        else:
            estado, nombre = resultado
            if estado == "Hundido":
                print(f"¡Hundido! Has destruido el {nombre}")
            else:
                print(f"¡Tocado!")


# ==========================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================

if __name__ == "__main__":
    # 1. Demostración Parte Estructurada
    print("=== TEST PARTE 1: RECORRIDO ESTRUCTURADO ===")
    matriz_simple = [[0] * 10 for _ in range(10)]
    matriz_simple[0][0] = 1  # Submarino
    matriz_simple[1][1] = 4  # Parte de Portaaviones
    total_p = recorrerTablero(matriz_simple)
    print(f"Total partes encontradas: {total_p}")

    # 2. Demostración Parte Objetos
    print("\n=== TEST PARTE 2: SISTEMA DE OBJETOS ===")
    partida = Juego()

    # Ataque a Submarino (Vida 1 -> Hundido)
    partida.lanzar_ataque(0, 0)

    # Ataques a Buque (Vida 2)
    partida.lanzar_ataque(5, 3)  # Tocado
    partida.lanzar_ataque(6, 3)  # Hundido

    # Ataque al agua
    partida.lanzar_ataque(9, 9)


