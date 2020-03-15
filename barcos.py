class Barco:
    def __init__(self, tamanio, orientacion, locacion):
        self.tamanio = tamanio
        self.locacion = locacion
        self.orientacion = orientacion
        
   
    
    def crear_barcos(self,fila,columna,tablero):
      	if self.orientacion == 'horizontal':
      	    if self.locacion['fila'] in range(fila):
      	  	    for index in range(self.tamanio):
      	  	        if self.locacion['col'] + index in range(columna):
      	  	            tablero[self.locacion['fila']][self.locacion['col']+index] = 'P'
      	  	            print('error')
      	    else:
      	  	    print('error')
      	else:
      	    if self.locacion['col'] in range(fila):
      	  	    for index in range(self.tamanio):
      	  	        if self.locacion['fila'] + index in range(columna):
      	  	            tablero[self.locacion['fila']+index][self.locacion['col']] = 'P'
      	  	        else:
      	  	            print('error')
      	    else:
      	  	    print('error')
    def mostrar(self):
        return f'tamanio:{self.tamanio}'