from usuario import Usuario
from random import randint
from barcos import Barco
from comunicador import Comunicador
from portaavion import PortaAvion
from submarino import Submarino
def verificar_username_existe(username):
    try:
        all_users = open('BaseDeDatos.txt', 'r').readlines()# Otra forma de acceder a un archivo
        for user in all_users:
            usuario = user[:-1].split(',') # [:-1] para quitar el salto de linea
            if usuario[0] == username:
                return True
        return False
    except FileNotFoundError:
        print('Todavia no se ha registrado ningun usuario')
        return False

def buscar_usuario(username):
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        if usuario[0] == username:
            return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])

def registrar():
    '''Funcion para ingresar un nuevo usuario'''
    contador=0
    validez=True
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numeros= ['1','2','3','4','5','6','7','8','9','0','']
    validez2=False
    

    while validez== True:
        contador=0 
    
        username= input('Usuario: ')
        
        for i in username:
            '''Valida que el usuario no contenga espacios o mayusculas'''
            if i==' ':
                contador+=1
            if i in mayusculas:
                contador+=1
        
        if len(username) > 30:
            '''Valida que el usuario no contenga mas de 30 caracteres'''
            contador+=1
       
                
        if contador>=1:
            print('Usuario Incorrecto.\nPorfavor verifique que el usuario contenga menos de 30 caracteres, no contenga mayusculas ni espacios.')
            print('-'*30)
        elif verificar_username_existe(username):
            '''Valida que el usuario que se ingresa no se repita'''
            print('Usuario Existente.\nPor favor ingrese otro usuario')
                
            
        elif username=='':
            '''Valida que el usuario no de enter sin ningun caracter'''
            print('Ingresa algun caracter')
            print('-'*93)
        elif len(username)<=3:
            print('Ingrese mas de 3 caracteres')

            
        else:
            validez=False      
            validez2=True 
        
        
    print('-'*19)
    while validez2==True:
        contador=0
        nombre=input('Nombre Completo: ')
        for i in nombre:
            if i in numeros:
                contador+=1
        if contador>=1:
            print('No ingrese numeros. Ingrese solo letras.\nVuelve a intentarlo')
            print('-'*19)
        else:
            '''Coloca la primera letra de cada nombre o apellido en un mayuscula'''
            nombre=nombre.title()
            validez2=False
    print(nombre)
    
    
    print('-'*19)
    while True:
        '''Valida que la edad este ente 5 y 100 años, y que sea solo caracter numerico'''
        try:
            edad=int(input('Edad: '))
            while edad<=5 or edad>=100 :
                print ('Edad incorrecta. \nverifique que este ingresando una edad valida.')
                print('-'*19)
                edad=int(input('Edad: '))
            break
        except ValueError:
            print('Edad Incorrecta.\nPor favor ingrese un numero')
            print('-'*19)
               
                    
                
    print('-'*19)            
    while True:
        '''Valida que solo ingrese m o f'''
        genero=input('Genero (Masculino(M) , Femenino(F)): ')
        genero.lower
        if genero=='m':
            genero='Masculino'
            print(genero)
            break
        elif genero =='f':
            genero='Femenino'
            print(genero)
            break
        else:
            if genero=='':
                '''Valida que no haga enter sin escribir nada'''
                print('No deje espacio en blanco')
            else:
                print('Ingrese una letra valida (m o f)')
                print('-'*93)
    usuario = Usuario(username, nombre, edad, genero,disparos=0,puntos=0,intentos=0,disparos_ganar=0)
    '''Agrega el usuario insertado en la Base de Datos'''
    with open("BaseDeDatos.txt", "a+") as bd: #El a+ es por si el archivo no se ha creado entonces se crea
        bd.write("{},{},{},{},{},{},{},{}\n".format(username, nombre, edad, genero,0,0,0,0))
    print('\tUsuario: ', usuario.username, ' registrado correctamente')
    return Usuario
   
   

def ver(edit = False):
    '''
    Funcion para ver los usuarios en la base de datos
    '''
    print(
        '''
        Estos son los usuarios registrados actualmente:
        '''
    )
    usuarios = []
    with open("BaseDeDatos.txt", "r") as bd:
        datos = bd.readlines()
    for dato in datos:
        usuario = dato[:-1].split(',') # [:-1] para quitar el salto de linea
        usuarios.append(Usuario(usuario[0], usuario[1], usuario[2], usuario[3]))
        #print(i+1, " - Estudiante {} de {} años, titular de la cedula {} y el carnet {} estudia {}".format(estudiante.nombre, estudiante.edad, estudiante[1], estudiante[2], estudiante[3]))
    #usuarios = sorted(usuarios, key= lambda user: user.username)
    if not edit:
        usuarios.sort(key= lambda user: user.username)
    for i, user in enumerate(usuarios):
        print('-'*5, i+1, '-'*5)
        print(user)


def actualizar(seleccion):

    '''
    Funcion que permite actualizar atributos de los usuarios registrados en la base de datos
    '''
    contador=0
    validez=True
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numeros= ['1','2','3','4','5','6','7','8','9','0','']
    
    print('''
    ¿Qué atributo desea modificar?
    1 - Usuario
    2 - Nombre
    3 - Edad
    4 - Género
    ''')
    selec  = int(input('''
    Seleccione una opción
    '''))

    with open("BaseDeDatos.txt", 'r') as bd:
        
        datos = bd.readlines()
        
        usuario = datos[seleccion - 1][:-1].split(',')
    while True:
        try:
            if selec==1:

                while validez==True:
                    contador=0

                    usuario[0] = input("Ingrese el nuevo usuario: ")
                    for i in usuario[0]:
                        if i==' ':
                            contador+=1
                    if i in mayusculas:
                        contador+=1

                    if len(usuario[0]) > 30:
                    
                        contador+=1


                    if contador>=1:
                        print('Usuario Incorrecto.\nPorfavor verifique que el usuario       contenga menos de 30 caracteres, no contenga mayusculas ni      espacios.')
                        print('-'*30)
                    elif verificar_username_existe(usuario[0]):
                        '''Valida que el usuario que se ingresa no se repita'''
                        print('Usuario Existente.\nPor favor ingrese otro usuario')


                    elif usuario[0]=='':
                        '''Valida que el usuario no de enter sin ningun caracter'''
                        print('Ingresa algun caracter')
                        print('-'*93)
                    elif len(usuario[0])<=3:
                        print('Ingrese mas de 3 caracteres')


                    else:
                        validez=False      

                
                nuevo_valor = ''
                for i in range(len(usuario)):
                    if i != len(usuario) -1:
                        nuevo_valor += usuario[i] + ','
                    else:
                        nuevo_valor += usuario[i] + '\n'
                datos[seleccion - 1] = nuevo_valor
                with open("BaseDeDatos.txt", "w") as bd:
                    bd.writelines(datos)
                break
            elif selec==2:
                while validez==True:
                    usuario[1] = input("Ingrese el nuevo nombre: ")
                    for i in usuario[1]:
                        if i in numeros:
                            contador+=1
                    if contador>=1:
                        print('No ingrese numeros. Ingrese solo letras.\nVuelve a intentarlo')
                        print('-'*19)
                    else:
                        '''Coloca la primera letra de cada nombre o apellido en un mayuscula'''
                        usuario[1]=usuario[1].title()
                        validez=False
                nuevo_valor = ''
                for i in range(len(usuario)):
                    if i != len(usuario) -1:
                        nuevo_valor += usuario[i] + ','
                    else:
                        nuevo_valor += usuario[i] + '\n'
                datos[seleccion - 1] = nuevo_valor
                with open("BaseDeDatos.txt", "w") as bd:
                    bd.writelines(datos)
                break
            elif selec==3:
                while True:
                    '''Valida que la edad este ente 5 y 100 años, y que sea solo        caracter numerico'''
                    try:
                        usuario[2] = int(input("Ingrese la nueva edad: "))
                        while usuario[2]<=5 or usuario[2]>=100 :
                            print ('Edad incorrecta. \nverifique que este ingresando        una edad valida.')
                            print('-'*19)
                            usuario[2]=int(input("Ingrese la nueva edad: "))

                        break
                    except ValueError:
                        print('Edad Incorrecta.\nPor favor ingrese un numero')
                        print('-'*19)


                nuevo_valor = ''
                for i in range(len(usuario)):
                    if i != len(usuario) -1:
                        nuevo_valor += str(usuario[i]) + ','
                    else:
                        nuevo_valor += usuario[i] + '\n'
                datos[seleccion - 1] = nuevo_valor
                with open("BaseDeDatos.txt", "w") as bd:
                    bd.writelines(datos)
                break
            elif selec==4:
                while True:
                    '''Valida que solo ingrese m o f'''
                    usuario[3] = input("Ingrese el nuevo genero (m)masculino o (f)femenino: ")
                    usuario[3].lower
                    if usuario[3]=='m':
                        usuario[3]='Masculino'
                        print(usuario[3])
                        break
                    elif usuario[3] =='f':
                        usuario[3]='Femenino'
                        print(usuario[3])
                        break
                    else:
                        if usuario[3]=='':
                            '''Valida que no haga enter sin escribir nada'''
                            print('No deje espacio en blanco')
                        else:
                            print('Ingrese una letra valida (m o f)')
                            print('-'*19)

                nuevo_valor = ''
                for i in range(len(usuario)):
                    if i != len(usuario) -1:
                        nuevo_valor += usuario[i] + ','
                    else:
                        nuevo_valor += usuario[i] + '\n'
                datos[seleccion - 1] = nuevo_valor
                with open("BaseDeDatos.txt", "w") as bd:
                    bd.writelines(datos)
                break
        except ValueError:
            print('Opcion Incorrecta')
        
        



    

def eliminar(seleccion):
    '''
    Funcion para eliminar un usuario de la base de datos
    '''
    with open("BaseDeDatos.txt", "r") as bd:
        lines = bd.readlines()
        suprimir = lines[seleccion - 1]
    with open("BaseDeDatos.txt", "w") as bd:
        for line in lines:
            if line != suprimir:
                bd.write(line)
def comenzar_juego():
    intentos=0
    contador=0
    validez=True
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
    

    while validez== True:
        contador=0 
    
        username= input('Ingrese un usuario Existente.\nUsuario: ')
        
        for i in username:
            '''Valida que el usuario no contenga espacios o mayusculas'''
            if i==' ':
                contador+=1
            if i in mayusculas:
                contador+=1
        
        if len(username) > 30:
            '''Valida que el usuario no contenga mas de 30 caracteres'''
            contador+=1
       
                
        if contador>=1:
            print('Usuario Incorrecto.\nPorfavor verifique que el usuario contenga menos de 30 caracteres, no contenga mayusculas ni espacios.')
            print('-'*30)
                
            
        elif username=='':
            '''Valida que el usuario no de enter sin ningun caracter'''
            print('Ingresa algun caracter')
            print('-'*93)
        elif len(username)<=3:
            print('Ingrese mas de 3 caracteres')

            
        else:
            if verificar_username_existe(username):
                print('Usuario Verificado.')
                intentos+=1
                validez=False
            
            else:
                print('El usuario no existe. Porfavor ingresa un usario existente')
                  
    
    fila=10
    columna=10
    oceano=[]
    tablero=[]
    for i in range(fila):
        '''Crea dos tableros'''
        '''Matriz falsa''' 
        tablero.append(["O"]*columna)
        '''Matriz de juego'''
        oceano.append(['O']*columna)



    def ubicaciones_disponibles(tamanio, orientacion):
        '''verifica las opciones disponibles'''
        locacion = []

        if orientacion != 'horizontal' and orientacion != 'vertical':
            raise ValueError("Orientation must have a value of either 'horizontal' or   'vertical'.")

        if orientacion == 'horizontal':
            fila_random = randint(0, fila-1)
            columna_random = randint(0, columna - tamanio + 1)
        elif orientacion == 'vertical':
            fila_random = randint(0, fila - tamanio + 1)
            columna_random = randint(0, columna-1)

        if orientacion == 'horizontal':
            if columna_random + tamanio <= columna and ('P' not in tablero[fila_random] [columna_random:columna_random+tamanio]):
                locacion = {'fila': fila_random, 'col': columna_random}
        elif orientacion == 'vertical':
            if fila_random+tamanio <= fila and 'P' not in [tablero[i][columna_random] for i in  range(fila_random, fila_random+tamanio)]:
                locacion = {'fila': fila_random, 'col': columna_random}
            

      
        if locacion:
            '''verifica bordes finales'''
            if orientacion == 'horizontal':
                if (columna_random-1 >= 0 and columna_random+tamanio+1 < columna and ('P' !=    tablero[fila_random][columna_random+tamanio+1]) and ('P' != tablero    [fila_random][columna_random-1])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random-1 >= 0 and columna_random+tamanio+1 >= columna and ('P'    != tablero[fila_random][columna_random-1])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random+tamanio+1 < columna and columna_random-1 < 0 and ('P' !=   tablero[fila_random][columna_random+tamanio+1])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                else:
                    locacion = []

            elif orientacion == 'vertical':
                if (fila_random-1 >= 0 and fila_random+tamanio+1 < fila and ('P' != tablero [fila_random-1][columna_random]) and ('P' != tablero[fila_random+tamanio+1]  [columna_random])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 < 0 and fila_random+tamanio+1 < fila and ('P' != tablero    [fila_random+tamanio+1][columna_random])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 >= 0 and fila_random+tamanio+1 >= fila and ('P' != tablero  [fila_random-1][columna_random])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                else:
                    locacion = []

          
        if locacion:
            '''Verifica bordes laterales'''
            if orientacion == 'horizontal':
                if (fila_random-1 >= 0 and fila_random+1 < fila and ('P' not in tablero [fila_random+1][columna_random:columna_random+tamanio]) and ('P' not in tablero  [fila_random-1][columna_random:columna_random+tamanio])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 < 0 and fila_random+1 < fila and ('P' not in tablero    [fila_random+1][columna_random:columna_random+tamanio])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (fila_random-1 >= 0 and fila_random+1 >= fila and ('P' not in tablero  [fila_random-1][columna_random:columna_random+tamanio])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                else:
                    locacion = []
            if orientacion == 'vertical':
                if (columna_random-1 >= 0 and columna_random+1 < columna and ('P' not in    [tablero[i][columna_random-1] for i in range(fila_random, fila_random+tamanio)]     and 'P' not in [tablero[i][columna_random+1] for i in range(fila_random,   fila_random+tamanio)])):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random-1 < 0 and columna_random+1 < columna and ('P' not in   [tablero[i][columna_random+1] for i in range(fila_random, fila_random+tamanio)]   )):
                    locacion = {'fila': fila_random, 'col': columna_random}
                elif (columna_random-1 >= 0 and columna_random+1 >= columna and ('P' not in     [tablero[i][columna_random-1] for i in range(fila_random, fila_random+tamanio)] )):
                    locacion = {'fila': fila_random, 'col': columna_random}
            else:
                locacion = []
        

        if not locacion:
            return 'None'
        else:
            return locacion


    def selecciona_ubicacion(tamanio):
        '''verifica que la posicion de los barcos sea horizontal o vertical'''
        orientacion = 'horizontal' if randint(0, 1) == 0 else 'vertical'
        locacion = ubicaciones_disponibles(tamanio, orientacion)
        
        print(locacion)
        if locacion == 'None':
            return 'None'
        else:
            return {'locacion': locacion, 'tamanio': tamanio, 'orientacion': orientacion}
       
    


    def print_tablero(tablero):
        '''Imprime el tablero'''
        print("\n  " + " ".join(str(x) for x in range(0, columna )))
        for r in range(fila):
            print(str(r) + " " + " ".join(str(c) for c in tablero[r]))
        print()


    
    numero_barcos = 0
    '''Crea Barcos de 3'''
    while numero_barcos < 1:
        barco_info = selecciona_ubicacion(3)
        
        if barco_info == 'None':
            continue
        else:

            Barco(barco_info['tamanio'], barco_info['orientacion'], barco_info['locacion']).crear_barcos(fila,columna,tablero)
            numero_barcos += 1
            
    del numero_barcos

    '''Crea Barcos de 2 casillas'''
    numero_barcos = 0
    while numero_barcos < 1:
        barco_info = selecciona_ubicacion(2)
        if barco_info == 'None':
            continue
        else:
            Barco(barco_info['tamanio'], barco_info['orientacion'], barco_info['locacion']).crear_barcos(fila,columna,tablero)
            
            numero_barcos += 1
    del numero_barcos


    '''Crea barcos de 1 casilla'''
    numero_barcos = 0
    
    while numero_barcos < 4:
        barco_info = selecciona_ubicacion(1)
        
        if barco_info == 'None':
            continue
        else:
            Barco(barco_info['tamanio'], barco_info['orientacion'], barco_info['locacion']).crear_barcos(fila,columna,tablero)
            
            numero_barcos += 1
    del numero_barcos
    
    
    





    

    print_tablero(tablero)
    print('-'*10)
    print_tablero(oceano)

    def juego(oceano,tablero):
        '''Valida los disparos y los puntajes'''
        hundir_flota=0
        disparos_repetidos=0
        disparos_realizados=0
        puntaje=0
        disparos_ganar=0
        '''Funcion para generar los disparos y validarlos'''
        while True:
            while True:
                try:
                    ingresar_fila= int(input('Fila: '))
                    ingresar_columna= int(input('Columna: '))
                    disparos_realizados+=1
                    if disparos_realizados==3:
                        print('Son muchos disparos. Perdiste!\nTienes que mejorar')
                        break
                    
                    if ingresar_fila<0 or ingresar_columna<0 or ingresar_fila>10 or     ingresar_columna>10:
                        print('Esto no esta en el oceano')

                    elif tablero[(ingresar_fila)][(ingresar_columna)]=='P':
                        oceano[(ingresar_fila)][(ingresar_columna)]='F'
                        tablero[(ingresar_fila)][(ingresar_columna)]='F'
                        print_tablero(oceano)
                        puntaje+=10
                        hundir_flota+=1
                        print('Le diste a un barco')
                    


                    else:
                        if oceano[(ingresar_fila)][(ingresar_columna)] == "X":
                            print('Ya la seleccionaste')
                            disparos_repetidos+=1
                        
                        else:
                            oceano[(ingresar_fila)][(ingresar_columna)] = "X"
                            tablero[(ingresar_fila)][(ingresar_columna)] = "X"
                            print_tablero(oceano)
                            puntaje-=2
                            print('incorrecto')
                        
                    if hundir_flota==9:
                        break
                
                    print('')
                except ValueError:
                    print('Ingresa un caracter valido')
            if disparos_realizados==9:
                print('¿Eres un robot?')
                disparos_ganar=disparos_realizados
            elif disparos_realizados>9 and disparos_realizados<45:
                print('Excelente estrategia!')
                disparos_ganar=disparos_realizados
            elif disparos_realizados>=45 and disparos_realizados<70:
                print('Buena Estrategia; pero hay que mejorar')
                disparos_ganar=disparos_realizados
            
            

            print(f'''
            Usuario: {username}
            Cantidad de disparos realizados: {disparos_realizados}
            Puntaje Total: {puntaje}
            Cantidad de disparos repetidos: {disparos_repetidos}
            Flota:
            ''' )
            print_tablero(tablero)

            with open("BaseDeDatos.txt", "r") as bd:
                datos=bd.readlines()
                for i in range(len(datos)):
                    usuario= datos[i][:-1].split(',')
                    nuevo_valor=''
                    if usuario[0]==username:
                        usuario[4]=int(usuario[4])+disparos_realizados

                    for a in range(len(usuario)):
                        if a!=len(usuario)-1:
                            nuevo_valor+=str(usuario[a])+ ','
                
                
                        else:
                            nuevo_valor+=str(usuario[a])+'\n'
                
                    datos[i]=nuevo_valor
                    with open('BaseDeDatos.txt','w') as bd:
                        bd.writelines(datos)
            with open("BaseDeDatos.txt", "r") as bd:
                datos2=bd.readlines()
                for i in range(len(datos)):
                    usuario= datos2[i][:-1].split(',')
                    nuevo_valor=''
                    if usuario[0]==username:
                        usuario[5]=int(usuario[5])+puntaje

                    for a in range(len(usuario)):
                        if a!=len(usuario)-1:
                            nuevo_valor+=str(usuario[a])+ ','
                
                
                        else:
                            nuevo_valor+=str(usuario[a])+'\n'
                
                    datos2[i]=nuevo_valor
                    with open('BaseDeDatos.txt','w') as bd:
                        bd.writelines(datos2)
            with open("BaseDeDatos.txt", "r") as bd:
                datos3=bd.readlines()
                for i in range(len(datos)):
                    usuario= datos2[i][:-1].split(',')
                    nuevo_valor=''
                    if usuario[0]==username:
                        usuario[7]=disparos_ganar

                    for a in range(len(usuario)):
                        if a!=len(usuario)-1:
                            nuevo_valor+=str(usuario[a])+ ','
                
                
                        else:
                            nuevo_valor+=str(usuario[a])+'\n'
                
                    datos3[i]=nuevo_valor
                    with open('BaseDeDatos.txt','w') as bd:
                        bd.writelines(datos3)

            with open("BaseDeDatos.txt", "r") as bd:
                datos4=bd.readlines()
                for i in range(len(datos)):
                    usuario= datos4[i][:-1].split(',')
                    nuevo_valor=''
                    if usuario[0]==username:
                        usuario[6]=int(usuario[6])+intentos

                    for a in range(len(usuario)):
                        if a!=len(usuario)-1:
                            nuevo_valor+=str(usuario[a])+ ','
                
                
                        else:
                            nuevo_valor+=str(usuario[a])+'\n'
                
                    datos4[i]=nuevo_valor
                    with open('BaseDeDatos.txt','w') as bd:
                        bd.writelines(datos4)
            
  
            break

   
    

    juego(oceano,tablero)

def estadisticas():
    with open("BaseDeDatos.txt","r") as bd:
        usernames=bd.readlines()
        contador_generos=[]
        contador_generos.append(usernames)
        print(estadisticas)
def usuarios_mas_jugados():
    '''Verifica cuales son los usuarios que mas juegan'''
    edad_5_18=0
    edad_19_45=0
    edad_46_60=0
    edad_61_100=0
    with open("BaseDeDatos.txt", 'r') as bd:
        datos = bd.readlines()
    for i in datos:
        usuario=i[:-1].split(',')
        if int(usuario[2])>5 and int(usuario[2])<=18:
            edad_5_18+=1
        if int(usuario[2])>18 and int(usuario[2])<=45:
            edad_19_45+=1
        if int(usuario[2])>45 and int(usuario[2])<=60:
            edad_46_60+=1
        if int(usuario[2])>60 and int(usuario[2])<=100:
            edad_61_100+=1
        print(f'Los usarios que juegan de acuerdo a las edades son:\n[5-18 años]={edad_5_18}\n[19-45 años]={edad_19_45}\n[46-60 años]={edad_46_60}\n[61-100 #años]={edad_61_100}')
        print('\n')

    if edad_5_18>edad_19_45 and edad_5_18>edad_46_60 and edad_5_18>edad_61_100:
        print('Los usuarios que mas juegan son los de 5 a 18 años.')
    elif edad_19_45>edad_5_18 and edad_19_45>edad_46_60 and edad_19_45>edad_61_100:
        print('Los usuarios que mas juegan son los de 19 a 45 años.')
    elif edad_46_60>edad_5_18 and edad_46_60>edad_19_45 and edad_46_60>edad_61_100:
        print('Los usuarios que mas juegan son los de 46 a 60 años.')
    elif edad_61_100>edad_5_18 and edad_61_100>edad_19_45 and edad_61_100>edad_46_60:
        print('Los usuarios que mas juegan son los de 61 a 100 años.')
        
    

def puntos_generos():
    '''Suma los puntos totales por genero'''
    lista_m=[]
    lista_f=[]
    with open("BaseDeDatos.txt", 'r') as bd:
        datos = bd.readlines()
    for i in datos:
        
        
        usuario=i[:-1].split(',')
        #print(usuario)
    
        
    
        if usuario[3]=='Masculino':
            #for i in range(len(datos)):
            lista_m.append(int(usuario[5]))
            sumar_m=sum(lista_m)

    
        elif usuario[3]=='Femenino':
            lista_f.append(int(usuario[5]))
            sumar_f=sum(lista_f)
    #print(hola)
    print(f'La cantidad de puntos por genero es:\nFemenino: {sumar_f}\nMasculino: {sumar_m}')
            

    
            
            
        
        
            #print(variable)
            #cantidad_masculino=sum ()
        #elif usuario[3]=='Femenino':
        #    cantidad_femenino=sum(int(usuario[5]))
    #print(cantidad_masculino)


def promedios():
    '''Calcula los promedios de disparos para ganar.'''
    intentos=[]
    disparos_gan=[]
    with open("BaseDeDatos.txt", 'r') as bd:
        datos = bd.readlines()
    for i in datos:
        usuario=i[:-1].split(',')
        intentos.append(int(usuario[6]))
        disparos_gan.append(int(usuario[7]))
    
        sumar_i=sum(intentos)
        sumar_d=sum(disparos_gan)
        promedio=sumar_d//sumar_i

    print(f'El promedio de los disparos realizados para ganar es de: {promedio}')


def top_10():
    with open("BaseDeDatos.txt", 'r') as bd:
        datos = bd.readlines()

def main():
    promedios()
    
    por= PortaAvion(1,'Porta Avion',3,1,{'fila': 5, 'col': 5},'aterrizar helicópteros en él para el transporte de tropas')
    com= Comunicador(1,'Comunicador',2,1,{'fila': 5, 'col': 5},'comunicarse con tierra y los otros miembros de la flota ')
    sub= Submarino(4,'Submarinos',1,1,{'fila': 5, 'col': 5},'Tiene la capacidad de poder sumergirse y emerger del agua')
    print("Bienvenido al juego de Batalla Naval")
    print('''
    Este juego consiste en descubrir la flota enenmiga. Que estara de modo alazar y esta flota esta conformada por los siguientes barcos:
    {}
    {}
    {}
    
    Nota: Para jugar por primera vez debe crear un usuario primero.
'''.format(por.mostrar(),com.mostrar(),sub.mostrar()))
    
    while True:
        while True:
            print('''
    ¿Qué desea Hacer?
    1 - Registrar un usuario
    2 - Jugar nuevo juego
    3 - Ver un usuario
    4 - Actualizar un usuario
    5 - Eliminar un usario

''')

            seleccion = input('''
    Seleccione una opción:  
            ''')

            if seleccion == '1':
                usuario = registrar()
                print(usuario)
                break
                
                    
            elif seleccion == '2':
                comenzar_juego()
                break
            elif seleccion =='3':
                ver()
                break
            elif seleccion == '4':
                ver(edit = True)
                seleccion = int(input("Seleccione el usuario que desee actualizar: "))
                actualizar(seleccion)
                break
            elif seleccion == '5':
                ver()
                seleccion = int(input("Seleccione el usuario que desee eliminar: "))
                eliminar(seleccion)
                break
            else:
                print("Seleccione una opción correcta.")
        
        volver_menu=input('desea volver al menu? Si(s) o No(n)')

        #if volver_menu.lower()!='s' or volver_menu.lower()!='n':
        #    print('opcion incorrecta.')

        if volver_menu.lower()=='n':
            
            break    
        elif volver_menu.lower()=='s':
            continue
        





main()