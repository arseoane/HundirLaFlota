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

        # Si hay impacto, se llama al método de la clase Nave.
        resultado_estado = objetivo.recibir_disparo()
        return (resultado_estado, objetivo.nombre)
