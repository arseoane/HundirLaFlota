# Examen
## 24/03/2026

### Objetivo:
Lograr desarrollar la clase *casilla*.

```python
class Casilla:
    def __init__(self):
        self.ocupante = None  # Aquí se guarda un objeto Nave si la casilla está ocupada, o None si está vacía
        self.revelada = False # Indica si la casilla ya ha sido atacada

    def disparar(self):
        self.revelada = True  # Marcamos la casilla como revelada tras el disparo
        if self.ocupante:
            # Si hay una nave, se le aplica el impacto
            return self.ocupante.recibir_impacto()
        return False  # Si no hay nave, no se hunde nada

```

