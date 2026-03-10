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


