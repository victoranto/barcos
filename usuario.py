class Usuario:
    def __init__(self, username, nombre, edad, genero, disparos = 0,puntos=0,intentos=0,disparos_ganar=0):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.disparos = disparos
        self.puntos = puntos
        self.intentos= intentos
        self.disparos_gana=disparos_ganar

    def __str__(self):
        return 'Usuario: {}\nNombre completo: {}\nEdad: {}\nGenero: {}\n'.format(self.username, self.nombre, self.edad, self.genero)