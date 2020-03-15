from barcos import Barco
class Submarino(Barco):
    def __init__(self,cantidad, nombre,tamanio, orientacion, locacion,habilidad):
        self.habilidad=habilidad
        self.nombre=nombre
        self.cantidad=cantidad
        super().__init__(tamanio,orientacion,locacion)
    def mostrar(self):
        return f'{self.cantidad} {self.nombre} de {self.tamanio} posicion(es).\nTiene la habilidad de {self.habilidad}.'