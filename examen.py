import json
import re

def parse_json (nombre_archivo:str):
    lista = []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]

    return lista

lista_jugadores = parse_json("/home/emilio/Documentos/Programacion y Laboratorio 1/0Examen/dt.json")

"""
Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
Nombre Jugador - Posición. Ejemplo:
Michael Jordan - Escolta
"""

def obtener_nombre_un_jugador(un_jugador):
    nombre ='Nombre: {0}'.format(un_jugador["nombre"])
    
    return nombre

def obtener_nombre_un_jugador_y_posicion(un_jugador):
    nombre_posicion ='{0} - {1} \n'.format(un_jugador["nombre"],un_jugador["posicion"])
    
    return nombre_posicion

def mostrar_nombre_posicion_jugadores(lista:list):
    
    if len(lista) == 0:
        return -1
    else:
        for jugador in lista:
            nombre_y_pos = obtener_nombre_un_jugador_y_posicion(jugador)
            print (nombre_y_pos)

"""
Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.
"""

def obtener_datos_un_jugadores(jugador):
    estadistica = jugador["estadisticas"]

    return estadistica

def obtener_una_estadistica(lista:list, indice:int):
    if len(lista) == 0:
        return -1
    elif indice > len(lista):
        return -1
    else:
        estadisticas = obtener_datos_un_jugadores(lista[indice])

    return estadisticas

def mostrar_estadisticas(un_diccionario):

    for clave in un_diccionario.keys():

            un_valor = str(un_diccionario[clave])
            mensaje_a_mostrar = "{0}: {1} ".format(clave,un_valor)
            print (mensaje_a_mostrar)

"""
Después de mostrar las estadísticas de un jugador seleccionado por el usuario,
permite al usuario guardar las estadísticas de ese jugador en un archivo CSV. El
archivo CSV debe contener los siguientes campos: nombre, posición, temporadas,puntos totales, promedio de puntos por partido, rebotes totales, promedio de rebotes
por partido, asistencias totales, promedio de asistencias por partido, robos totales,
bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y
porcentaje de tiros triples.
"""

def guardar_archivo(nombre_archivo:str, dato): 
    result = False
    with open(nombre_archivo, "w+") as archivo:

        nombre_a_guardar = "{0} \n".format(dato['nombre'])
        resultado = archivo.write(nombre_a_guardar)
        
        for clave in dato['estadisticas'].keys():

            un_valor = str(dato['estadisticas'][clave])
            mensaje_a_guardar = "{0}: {1} \n".format(clave,un_valor)
            resultado = archivo.write(mensaje_a_guardar)
        
        if resultado ==0:
            print('fallo')
        else:
            print('exito')
            result = True
            
    return result

def guardar_un_jugador_estadisticas(un_jugador): 

    archivo = "/home/emilio/Documentos/Programacion y Laboratorio 1/0Examen/jugador_{}.csv".format(un_jugador['nombre'])
    return guardar_archivo(archivo,un_jugador)

"""
Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como
campeonatos de la NBA, participaciones en el All-Star y pertenencia al Salón de la
Fama del Baloncesto, etc.
"""

def buscar_por_nombre(ingreso_usuario:str, lista:list):
    for jugador in lista:
        nombre = jugador["nombre"]
        cohincidencias = bool(buscar_nombre_incompleto (nombre, ingreso_usuario))
        if cohincidencias == True:
            logros = de_lista_a_string(jugador["logros"])
            mensaje = 'Se encontro al jugador: {0}\nSus logros son: \n{1}\n\n'.format(jugador["nombre"],logros)
            return mensaje

def de_lista_a_string(lista:list)->str:
    cadena = "\n"
    cadena = cadena.join(lista)
    return cadena
    

def buscar_nombre_incompleto(texto_a_analizar:str, nombre_ingresado:str):
    patron = "{}".format(re.escape(nombre_ingresado))
    resultados = re.findall(patron, texto_a_analizar, re.IGNORECASE)
    return resultados

"""
Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream
Team, ordenado por nombre de manera ascendente.
"""

def quick_sort(lista_original:list,llave1,llave2, flag_orden:bool)->list:
    lista_nueva = lista_original[:]
    lista_de = []
    lista_iz = []
    if (len(lista_nueva) < 1):
        return lista_nueva
    else:
        pivot = lista_nueva[0] #dejar pivot como heroe aca asi se agrega completo a la lista que retorna, sino devuelve solo el dato ordenado
        for elemento in lista_nueva[1:]:
            if(elemento[llave1][llave2] > pivot[llave1][llave2]): #el pivot tiene que ser heroe key
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)

    lista_iz = quick_sort(lista_iz,llave1,llave2, True)
    lista_iz.append(pivot) #para pormedio sacar esta lista y puede andar

    lista_de = quick_sort(lista_de,llave1,llave2, True)
    lista_iz.extend(lista_de)

    return lista_iz

def mostrar_nombre_prom_pun_part(lista):
    for jugador in lista:
        nombre = jugador['nombre']
        promedio_punt_part = jugador['estadisticas']["promedio_puntos_por_partido"]
        print(nombre,promedio_punt_part)

def obtener_promedio(lista):
    total_puntos_por_partido = obtener_puntos_partido_team(lista)
    promedio = total_puntos_por_partido/len(lista)
    mensaje = 'El promedio general de todo el Dream Team es: {0}'.format(promedio)
    print(mensaje)

def obtener_puntos_partido_team(lista):
    suma_puntos = 0
    for indice in range(len(lista)):
        estadistica_un_jugador = obtener_una_estadistica(lista, indice)
        puntos_por_partido = obtener_puntos(estadistica_un_jugador)
        suma_puntos += puntos_por_partido
    return suma_puntos

def obtener_puntos(diccionario):  
    puntos = diccionario["promedio_puntos_por_partido"]
    return puntos


"""
Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es
miembro del Salón de la Fama del Baloncesto.
"""

def mostrar_si_es_miembro(logros:str):    
    return bool(re.search("Universitario", logros))

"""
Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
"""

def calcular_max(lista, llave):
    maximo_llave = None
    maximo_indice = None
    for indice in range(len(lista)):
        maximo = lista[indice]["estadisticas"][llave]
        if (indice == 0 or maximo_llave < maximo):
            maximo_llave = maximo
            maximo_indice = indice
    maximo_jugador = "nombre: {0} | {1}: {2}".format(lista[maximo_indice]["nombre"],llave,maximo_llave)

    return maximo_jugador

"""
Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado
más puntos por partido que ese valor
"""

def jugadores_mayor_al_imput(lista, llave, numero_ingresado):
    for indice in range(len(lista)):
        maximo = lista[indice]["estadisticas"][llave]
        if (numero_ingresado < maximo):
            jugador_mayor_imput = "nombre: {0} | {1}: {2}".format(lista[indice]["nombre"],llave,maximo)
            print(jugador_mayor_imput)


"""
17 Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
"""

def calcular_max_logros(lista, llave):
    maximo_llave = None
    maximo_indice = None
    for indice in range(len(lista)):
        maximo = len(lista[indice][llave])
        if (indice == 0 or maximo_llave < maximo):
            maximo_llave = maximo
            maximo_indice = indice
    maximo_jugador = "nombre: {0} | {1}: {2}".format(lista[maximo_indice]["nombre"],llave,maximo_llave)

    return maximo_jugador   

"""
Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
"""

def jugadores_mayor_al_imput_20(lista, llave, numero_ingresado):
    lista_mayor_input = []
    for jugador in lista:
        maximo = jugador["estadisticas"][llave]
        if (numero_ingresado < maximo):
            lista_mayor_input.append(jugador)
    return lista_mayor_input

def ordenar_por_posicion(lista_mayor:list,up = True):
    rango_a = len(lista_mayor)
    flag_swap = True

    while (flag_swap):
        flag_swap = False
        rango_a -= 1

        for indice_a in range(rango_a):
            if up == False and lista_mayor[indice_a]["posicion"] < lista_mayor[indice_a+1]["posicion"] \
            or up == True and lista_mayor[indice_a]["posicion"] > lista_mayor[indice_a+1]["posicion"]:
                lista_mayor[indice_a],lista_mayor[indice_a+1] = lista_mayor[indice_a+1],lista_mayor[indice_a]
                flag_swap = True

def mostrar_lista_ordenada(lista):
    for indice in range(len(lista)):
        nombre_posicion_mayor_imput = "nombre: {0} posicion: {1} | porcentaje_tiros_de_campo: {2}".format(lista[indice]["nombre"],lista[indice]["posicion"],lista[indice]["estadisticas"]["porcentaje_tiros_de_campo"])
        print(nombre_posicion_mayor_imput)

def imprimir_menu_desafio_5():

    print('1 Mostrar la lista de todos los jugadores del Dream Team.')
    print('2 Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas')
    print('3 Exportar jugador a CSV')
    print('4 Buscar por nombre y mostrar logros')
    print('5 Mostrar el promedio de puntos por partido de todo el equipo del Dream Team')
    print('6 Buscar por nombre y mostrar si es miembro del Salón de la Fama')
    print('7 Calcular y mostrar el jugador con la mayor cantidad de rebotes totales')
    print('8 Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo')
    print('9 Calcular y mostrar el jugador con la mayor cantidad de asistencias totales')
    print('10 Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor')
    print('11 Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor')
    print('12 Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor')
    print('13 Calcular y mostrar el jugador con la mayor cantidad de robos totales')
    print('14 Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales')
    print('15 Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor')
    print('16 Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.')
    print('17 Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos')
    print('18 Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor')
    print('19 Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas')
    print('20 Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior al valor')

    print()
    print('0 Salir')

    opcion = input("\nIngrese la opción deseada: ")
    
    return opcion

def respuesta_valida(texto):
    patron = r'^[0-9]+$'
    return bool(re.match(patron, texto))

def star_team_app(lista):
    while True:
        respuesta = imprimir_menu_desafio_5()
        respuesta_validada = respuesta_valida(respuesta)
        indice = None
        if (respuesta_validada != True):
            print('Error ingrese una opcion correcta')
        else:
            match respuesta:
                case '1':
                    print('\n')
                    mostrar_nombre_posicion_jugadores(lista_jugadores)
                    input('pulse cualquier tecla para continuar')
                case '2':
                    indice = int(input('ingrese un numero correspondiente al indice: '))
                    print('\n')
                    if indice > len(lista_jugadores):
                        print('error ingrese un indice valido')
                        input('pulse cualquier tecla para continuar')
                    else:
                        estadistica_un_jugador = obtener_una_estadistica(lista_jugadores, indice)
                        print(lista_jugadores[indice]['nombre'])
                        mostrar_estadisticas(estadistica_un_jugador)
                        print('\n')
                        input('pulse cualquier tecla para continuar')
                case '3':
                    if indice == None:
                        print('error primero usar el paso 2 \n')
                        input('pulse cualquier tecla para continuar')
                    else:
                        guardar_un_jugador_estadisticas(lista_jugadores[indice])
                        input('pulse cualquier tecla para continuar')
                case '4':
                    ingreso_busqueda = input('ingrese el nombre del jugador a buscar: ')
                    print('\n')
                    print(buscar_por_nombre(ingreso_busqueda, lista_jugadores))
                    input('pulse cualquier tecla para continuar')
                case '5':
                    print('\n')
                    lista_ordenada = quick_sort(lista,"estadisticas","promedio_puntos_por_partido", True)
                    mostrar_nombre_prom_pun_part(lista_ordenada)
                    obtener_promedio(lista_jugadores)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '6':
                    ingreso_busqueda = input('ingrese el nombre del jugador a buscar: ')
                    logros = buscar_por_nombre(ingreso_busqueda, lista_jugadores)
                    es_miembro = mostrar_si_es_miembro(logros)
                    if es_miembro == True:
                        print('NO es Miembro del Salon de la Fama del Baloncesto \n')
                        input('pulse cualquier tecla para continuar')
                    else:
                        print('Miembro del Salon de la Fama del Baloncesto \n')
                        input('pulse cualquier tecla para continuar')
                case '7':
                    print('\n')
                    print(calcular_max(lista_jugadores, "rebotes_totales"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '8':
                    print('\n')
                    print(calcular_max(lista_jugadores, "porcentaje_tiros_de_campo"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '9':
                    print('\n')
                    print(calcular_max(lista_jugadores, "asistencias_totales"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '10':
                    print('\n')
                    valor_ingresado = float(input('ingrese un valor numerico a evaluar'))
                    jugadores_mayor_al_imput(lista_jugadores, "promedio_puntos_por_partido", valor_ingresado)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '11':
                    print('\n')
                    valor_ingresado = float(input('ingrese un valor numerico a evaluar'))
                    jugadores_mayor_al_imput(lista_jugadores, "promedio_rebotes_por_partido", valor_ingresado)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '12':
                    print('\n')
                    valor_ingresado = float(input('ingrese un valor numerico a evaluar'))
                    jugadores_mayor_al_imput(lista_jugadores, "promedio_asistencias_por_partido", valor_ingresado)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '13':
                    print('\n')
                    print(calcular_max(lista_jugadores, "robos_totales"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '14':
                    print('\n')
                    print(calcular_max(lista_jugadores, "bloqueos_totales"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '15':
                    print('\n')
                    valor_ingresado = float(input('ingrese un valor numerico a evaluar'))
                    jugadores_mayor_al_imput(lista_jugadores, "porcentaje_tiros_libres", valor_ingresado)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '16':
                    print('\n')
                    lista_ordenada = quick_sort(lista,"estadisticas","promedio_puntos_por_partido", True)
                    mostrar_nombre_prom_pun_part(lista_ordenada[1:])
                    obtener_promedio(lista_ordenada[1:])
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '17':
                    print('\n')
                    print(calcular_max_logros(lista_jugadores, "logros"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '18':
                    print('\n')
                    valor_ingresado = float(input('ingrese un valor numerico a evaluar'))
                    jugadores_mayor_al_imput(lista_jugadores, "porcentaje_tiros_triples", valor_ingresado)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '19':
                    print('\n')
                    print(calcular_max(lista_jugadores, "temporadas"))
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '20':
                    print('\n')
                    valor_ingresado = float(input('ingrese un valor numerico a evaluar'))
                    lista_mas_grandes = jugadores_mayor_al_imput_20(lista_jugadores, "porcentaje_tiros_de_campo", valor_ingresado)
                    ordenar_por_posicion(lista_mas_grandes,up = True)
                    mostrar_lista_ordenada(lista_mas_grandes)
                    print('\n')
                    input('pulse cualquier tecla para continuar')
                case '0':
                    break

star_team_app(lista_jugadores)