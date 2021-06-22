import random

# DEFINICION FUNCIONES
# ********************

def elegirCategoria():
    """Selector de categoria. Podes generar tu categoría siguiendo <Categoria>:<Palabra>,<Palabra>"""
    try:
        categorias = open("categorias.txt","rt")
        categoriaLista = []
        for linea in categorias:
            categoria,palabras = linea.split(":")
            categoriaLista.append(categoria.capitalize())
        categorias.seek(0)
        seleccionarCategoria = input(f"Selecciona una categoria entre {categoriaLista}: ")
        while seleccionarCategoria.capitalize() not in categoriaLista:
            seleccionarCategoria = input("Seleccione una categoria valida: ")
        for linea in categorias:
            categoria,palabrasTotal = linea.split(":")
            if seleccionarCategoria.capitalize() == categoria.capitalize():
                palabrasTotal = palabrasTotal.strip("\n")
                categoria = categoria.capitalize()
                break
        palabrasTotal = palabrasTotal.split(",")    
        return palabrasTotal,categoria
    except FileNotFoundError as mensaje:
        print("No se puede abrir el archivo:",mensaje)
    except OSError as mensaje:
        print("ERROR:", mensaje)
    finally:
        try:
            categorias.close()
        except NameError:
            pass

def imprimir_matriz(matriz, fila = 0, columna = 0):
    tamaño = len(matriz)
    if columna == tamaño:
        print()
        columna = 0
        fila += 1
    if columna < tamaño and fila < tamaño:
        print(f"{matriz[fila][columna]:3}", end= "")
        imprimir_matriz(matriz, fila, columna + 1)

def leerPalabraFila(matriz, fila, cInicial, cFinal):
    pal = []
    for f in range(len(matriz)):
         for c in range(len(matriz)):
               if(f == fila and c >= cInicial and c <= cFinal):
                       pal.append(matriz[f][c])                     
    return pal

def leerPalabraCol(matriz, col, fInicial, fFinal):
    pal = []
    
    for f in range(len(matriz)):
         for c in range(len(matriz)):
               if(c == col and f >= fInicial and f <= fFinal):
                       pal.append(matriz[f][c])
                           
    return pal

def validadorPalabra(palabraEncontrada, palabrasTotal):
    
    validador = 0
    for i in range(len(palabrasTotal)):
        if(palabrasTotal[i].upper() == palabraEncontrada):
            validador = 1        
    
    return validador

def cambiarPalabraHorizontal(matriz, fila, cInicial, cFinal):
    
    for f in range(len(matriz)):
         for c in range(len(matriz)):
               if(f == fila and c >= cInicial and c <= cFinal):
                   matriz[f][c] = matriz[f][c].lower()
    
    return matriz

def cambiarPalabraVertical(matriz, col, fInicial, fFinal):
    
    for f in range(len(matriz)):
         for c in range(len(matriz)):
               if(c == col and f >= fInicial and f <= fFinal):
                   matriz[f][c] = matriz[f][c].lower()
    
    return matriz

def crearCoordenadasEnMatriz(matriz):
    tam = len( matriz )
    for i in range(tam):
        matriz[0][i] = str(i)
        matriz[i][0] = str(i) 

def ordenarPalabrasEnMatriz(matriz, palabras):
    tam = len( matriz )                                   
    orden = ["horiz", "vert"]
    coor_ocup = []
    for palabra in palabras:
        palabra_ubicada = 0
        intentos = 0
        tam_p = len(palabra)   
        while (palabra_ubicada < 1 and intentos < 10):
            elecc = random.choice(orden)
            coor = random.randint(1, tam - 1)
            despla = random.randint(1, tam - tam_p)
            if elecc == "horiz":
                cont_intentos_horiz = 0
                while cont_intentos_horiz < 10:
                    posib = []
                    cont_ocup = 0
                    # guardo en una lista las posibles coordenadas en la matriz 
                    for i in range( len(palabra) ):
                        posib.append(f'{coor}{despla + i}')
                    # recorro las dos listas, las coor8denadas ocupadas y las nuevas, para saber si se pisan
                    for i in range( len(coor_ocup) ):
                        for j in range( len(posib) ):
                            if coor_ocup[i] == posib[j]:
                                cont_ocup = cont_ocup + 1
                    # Si no hay coincidencias la palabra se acomoda en la matriz y se pone 1 en palabra ubicada y se asegura salir del while
                    if cont_ocup == 0: 
                        palabra_ubicada = 1
                        cont_intentos_horiz = 11
                        for i in range( len(palabra) ):
                            coor_ocup.append(f'{coor}{despla + i}')
                            matriz[coor][despla + i] = palabra[i].upper()
                    # Siempre se suma un intento
                    cont_intentos_horiz = cont_intentos_horiz + 1
            if elecc == "vert":
                cont_intentos_vert = 0
                while cont_intentos_vert < 10:
                    posib = []
                    cont_ocup = 0
                    # guardo en una lista las posibles coordenadas en la matriz 
                    for i in range( len(palabra) ):
                        posib.append(f'{despla + i}{coor}')
                    # recorro las dos listas, las coordenadas ocupadas y las nuevas, para saber si se pisan
                    for i in range( len(coor_ocup) ):
                        for j in range( len(posib) ):
                            if coor_ocup[i] == posib[j]:
                                cont_ocup = cont_ocup + 1
                    # Si no hay coincidencias la palabra se acomoda en la matriz y se pone 1 en palabra ubicada y se asegura salir del while
                    if cont_ocup == 0:
                        palabra_ubicada = 1
                        cont_intentos_vert = 11
                        for i in range( len(palabra) ):
                            coor_ocup.append(f'{despla + i}{coor}')
                            matriz[despla + i][coor] = palabra[i].upper()
                    # Siempre se suma un intento
                    cont_intentos_vert = cont_intentos_vert + 1
            # Se suma un intento al while principal
            intentos = intentos + 1


# MAIN / PROGRAMA PRINCIPAL
# *************************

# Inicio del Juego

print()
print(f"\n///SOPA DE LETRAS CON PYTHON///\n{'*'*31}\n")
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
tablaPuntajes = {}
jugar = "s"

while(jugar.lower() == "s"):
    
    # Inicio sesión Jugador
    
    palabrasAEncontrar = ()
    
    nombreJugador = input("Nombre del jugador: ")
    tablaPuntajes[nombreJugador] = 0
    
    palabrasTotal,categoria = elegirCategoria()
    cont_PalabrasTotal = len(palabrasTotal)
    puntajeMinimo = (1/cont_PalabrasTotal) * 100
    print(f"El jugador {nombreJugador} selecciono la categoria: {categoria}\nLas palabras a buscar son: {palabrasTotal}")
    
    # Creación e Impresión de la Matriz

    matriz = [[random.choice(letras) for col in range(16)] for row in range(16)]
    crearCoordenadasEnMatriz(matriz)
    ordenarPalabrasEnMatriz(matriz, palabrasTotal)
    print()
    imprimir_matriz(matriz)
    print()
    
    while (jugar.lower() == "s" and len(palabrasAEncontrar) < cont_PalabrasTotal):
        
        forma = input("De qué forma se encuentra la palabra que acaba de encontrar?:\n\nPresione H, si la palabra esta horizontal\nPresione V, si la palabra esta Vertical\n")
        
        # Validacion de la Opciones
        
        while (forma.lower() != "h" and forma.lower() != "v"):
            print("Opcion ingresada incorrecta\n")
            forma = input("De qué forma se encuentra la palabra que acaba de encontrar?:\n\nPresione H, si la palabra esta horizontal\nPresione V, si la palabra esta Vertical\n")

        # Lectura Palabra Horizontal
        
        if(forma.lower() == "h"):

            while True:
                try:
                    fila = int(input("Ingrese numero de fila: "))
                    cInicial = int(input("Ingrese numero de columna incial: "))
                    cFinal = int(input("Ingrese numero de columan final: "))
                    assert fila > 0,"Valor ingresado Incorrecto. Ingrese un número positivo: "  
                    assert cInicial > 0,"Valor ingresado Incorrecto. Ingrese un número positivo: "
                    assert cFinal > 0,"Valor ingresado Incorrecto. Ingrese un número positivo: "
                    break
                except AssertionError as mensaje:
                    print(mensaje)
                except ValueError:
                    print("Valor ingresado Incorrecto. Ingrese un número positivo")
            
            palabraLista = leerPalabraFila(matriz, fila, cInicial, cFinal)
            print()
            palabraEncontrada = "".join(palabraLista)
            print(f"La palabra encontrada es: {palabraEncontrada.capitalize()}")
            print()
            #Validacion de la Palabra
            
            validador = validadorPalabra(palabraEncontrada, palabrasTotal)
            
            if(validador == 1):
                palabrasAEncontrar = palabrasAEncontrar + (palabraEncontrada,)
                tablaPuntajes[nombreJugador] = tablaPuntajes[nombreJugador] + puntajeMinimo
                print("Puntaje Total: ", tablaPuntajes[nombreJugador])
                print()
                matriz = cambiarPalabraHorizontal(matriz, fila, cInicial, cFinal)
                
                imprimir_matriz(matriz)
                print()
            else:
                print("\nPalabra indicada incorrecta\n")
                
        # Lectura Palabra Vertical
        
        elif(forma.lower() == "v"):
            
            while True:
                try:
                    col = int(input("Ingrese el numero de columna en el que se encuentra la palabra: "))
                    fInicial = int(input("Ingrese la fila en donde empieza la palabra: "))
                    fFinal = int(input("Ingrese la fila en donde termina la palabra: "))
                    assert col > 0,"Valor ingresado Incorrecto. Ingrese un número positivo: "  
                    assert fInicial > 0,"Valor ingresado Incorrecto. Ingrese un número positivo: "
                    assert fFinal > 0,"Valor ingresado Incorrecto. Ingrese un número positivo: "
                    break
                except AssertionError as mensaje:
                    print(mensaje)
                except ValueError:
                    print("Valor ingresado Incorrecto. Ingrese un número positivo")

            palabraLista = leerPalabraCol(matriz, col, fInicial, fFinal)
            print()
            
            palabraEncontrada = "".join(palabraLista)
            print(f"La palabra encontrada es: {palabraEncontrada.capitalize()}")
            print()
            #Validacion de la Palabra
            
            validador = validadorPalabra(palabraEncontrada, palabrasTotal)
            
            if(validador == 1):
                palabrasAEncontrar = palabrasAEncontrar + (palabraEncontrada,)
                tablaPuntajes[nombreJugador] = tablaPuntajes[nombreJugador] + puntajeMinimo
                print("Puntaje Total: ", tablaPuntajes[nombreJugador])
                print()
                matriz = cambiarPalabraVertical(matriz, col, fInicial, fFinal)
                imprimir_matriz(matriz)
                print()
            else:
                print("\nPalabra indicada incorrecta\n")
            
        print()
        
        # Menu de Sesión de Jugador
        if len(palabrasAEncontrar) < cont_PalabrasTotal:
            jugar = input("¿Desea seguir jugando con este jugador?: (Presione s para seguir y cualquier otra tecla para salir): ")
        else: 
            print("¡Felicitaciones! ¡Has encontrado todas las palabras!")
            print()
            
    # Menu Principal de Juego

    jugar = input("¿Desea jugar con un nuevo jugador?: (Presione s para seguir y cualquier otra tecla para salir): ")

print()
print("Tabla de puntajes de sopa de letras:")
for jugador, puntaje in tablaPuntajes.items():
    print(f"{jugador}: {puntaje}")

print("\n\nHasta la próxima!!\n\n")