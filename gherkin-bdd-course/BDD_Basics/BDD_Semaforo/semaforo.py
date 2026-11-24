class Semaforo:
    CICLO = ["rojo", "verde", "amarillo"]

    def __init__(self):
        self.indice = 0

    @property
    def color(self):
        return self.CICLO[self.indice]

    def avanzar(self):
        self.indice = (self.indice + 1) % len(self.CICLO)

    def pueden_avanzar_autos(self):
        return self.color == "verde"