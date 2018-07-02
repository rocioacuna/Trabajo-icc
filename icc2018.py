import os
import time
def guardar(lisa_de_alumnos, lista_de_mensajes, ID):                 #Es lo mismo que antes, solo que al estar en una funcion no consume memoria
    x = lisa_de_alumnos, lista_de_mensajes
    bool = True
    for i in x:
        string = ""
        for e in i:
            for u in e:
                string = string + str(u) +"-"
            string = string + "\n"
        if bool:
            string = string + str(ID)
            bool = False
            archivo = open("alumnos.txt","w")
            archivo.write(string)
        else:
            archivo = open("mensajes.txt", "w")
            archivo.write(string)
        archivo.close()
        

def menu():
    print("=============================")
    print("||     1. Crear            ||")
    print("||     2. Buscar           ||")
    print("||     3. Editar           ||")
    print("||     4. Eliminar         ||")
    print("||     5. Mensaje          ||")
    print("||     6. Ver historial    ||")
    print("||     7. Salir            ||")                                           
    print("=============================")
    print("Seleccione una opción del 1 al 6: ")
    opcion = str(input())
    return opcion


def fn():
    lista2 = ["Nombre nuevo: ", "Apellido Paterno nuevo: ", "Edad nueva: ", "Teléfono nuevo: "]
    alumno_nuevo = []                                                                                                 #Esta funcion es la entrada de datos estamdar, como al crear o editar un dato
    bool = True                                                                                                       # se tenia que meter la misma informacion, esta funcion evita que se repitan cosas
    for i in lista2:
        x = input(i)
        if i == "Edad nueva: " or i == "Teléfono nueva: ":           #  si es que se va a ingresar la edad o el telefono...
            if x.isdigit():                                           #  comprueba si es un entero
                alumno_nuevo.append(x)                                 #  si es asi continua
            else:
                del alumno_nuevo                                                            #si no es asi, imprime 
                print("Edad o teléfono solo pueden ser numeros.")                            #esto...
                wi = fn()                                                      #y vuelve a auto invocarse la funcion
                bool = False
                break
        else:
            alumno_nuevo.append(x)
    if bool:
        return alumno_nuevo
    else:
        return wi      


def crear(lista,ID):
    ID = int(int(ID) + 1)
    alumno_nuevo = fn()                                                                                                            #llamamos a la funcion de entrada de datos
    alumno_nuevo.append(str(ID))
    lista.append(alumno_nuevo)
    return lista, ID


def buscar(lista, valor_a_buscar):
    for i in lista:
        for e in i:
            if valor_a_buscar in e:
                print(e,"Encontrado en: ",i)
                break
    return None

def buscar_ID(lista, ID):
    i = 0                                                               #la funcion de buscar_id es usada al invocar la funcion editar o eliminar,
    bool = True                                                        # porque al ingresar un id, se tiene que recorrer toda la lista en busca dela posicion donde este el id
    while bool and i < len(lista):
        if int(lista[i][4]) == int(ID):
            bool = False
        else:
            i += 1                                  #si no lo encuentra retorna falso*******************
    if bool:
        return None
    return int(i)


def editar(lista, ID_Registro): 
    bool = True
    posicion = buscar_ID(lista, ID_Registro)
    if posicion == None:
        print("ID no encontrado.")
        bool = False
    else:
        alumno_modificado = fn()
    if bool:
        alumno_modificado.append(str(ID_Registro))
        lista[posicion] = alumno_modificado
        return lista


def eliminar(lista, ID_Registro):
    posicion = buscar_ID(lista, ID_Registro)
    if not posicion == None:                                           #si NO retorna falso, o vacio (nada=none), sino solo ignora todo y sigue el programa 
        print("Lista antes: ",lista_de_alumnos)
        lista.pop(posicion)
        print("Lista despues: ", lista_de_alumnos)
        return lista


def mensaje(emisor, receptor, mensaje, lista_de_mensajes):
    x = time.strftime("%c")
    mensaje = [emisor, receptor, mensaje, x]
    print(mensaje)
    lista_de_mensajes.append(mensaje) 
    return lista_de_mensajes


def ver_historial(lista_de_mensajes, lista_de_alumnos):
    emisor = []
    receptor = []
    for i in lista_de_mensajes:
        emisor.append(buscar_ID(lista_de_alumnos, int(i[0])))                                                #buscamos el id de cada receptor (i) en la lista de alumnos a traves de la funcion buscar_ID
        receptor.append(buscar_ID(lista_de_alumnos, int(i[1])))
        print(lista_de_mensajes)
    for e in range(len(lista_de_mensajes)):                                                                  #se imprime toda la vaina
        print(f"Mensaje {e}:\n  Emisor:\n     Nombre: {lista_de_alumnos[emisor[e]][0]}\n     Apellido: {lista_de_alumnos[emisor[e]][1]}\n  Receptor:\n     Nombre: {lista_de_alumnos[receptor[e]][0]}\n     Apellido: {lista_de_alumnos[receptor[e]][1]}\n  Fecha y hora: {lista_de_mensajes[e][3]}\n  Mensaje: {lista_de_mensajes[e][2]}\n \n")

def leer(algo):                                                                                    
    try:                                                                                          #como son 2 archivos, y los contatenamos de la misma forma
        archivo = open(algo, "r+")                                                                #es redundante hacer 2 veces el mismo proceso
        lista = archivo.readlines()                                                               #esta funcion puede tomar estos valores-----------------------
        archivo.close()

    except IOError:
        archivo = open(algo, "w+")
        lista_de_algo = []
        ID = -1
        if algo == "mensajes.txt":
            return lista_de_algo
        return lista_de_algo, ID

    else:
        lista_de_algo = []
        if algo=="alumnos.txt":
            x = len(lista)-1
        else:
            x = len(lista)
        for i in range(x):
            lista_de_algo.append(lista[i].split("-"))
            lista_de_algo[i].pop()
        if algo == "alumnos.txt":
            if len(lista):
                ID = lista[-1]
            else:
                ID = -1
            return lista_de_algo, ID
        else:
            return lista_de_algo
        

lista_de_alumnos, ID = leer("alumnos.txt")                                            #---------------   puede ser leer("alumnos.txt")
lista_de_mensajes = leer("mensajes.txt")                                              #------------------ o leer("mensajes.txt")
opcion = 0

while opcion != "7":
    
    opcion = menu()

    if opcion == "1":
        print("Seleccionó la opción Crear")
        lista_de_alumnos, ID = crear(lista_de_alumnos, ID)
        print("lista anterior: ", lista_de_alumnos)

    elif opcion == "2":
        print("Seleccionó la opción Buscar")
        valor_a_buscar = input("Ingrese el valor a buscar: ")
        buscar(lista_de_alumnos, valor_a_buscar)

    elif opcion == "3":
        print("Seleccionó la opción Editar")
        try:
            codigo_de_alumno = int(input("Ingrese el ID de registro de alumno a MODIFICAR: "))
            lista_de_alumnos = editar(lista_de_alumnos, codigo_de_alumno)
        except ValueError:
            print("Porfavor ingrese un entero.")
        

    elif opcion == "4":
        print("Seleccionó la opción Eliminar")
        try:
            codigo_de_alumno = int(input("Ingrese el ID de registro de alumnoa ELIMINAR: "))
            lista_de_alumnos = eliminar(lista_de_alumnos, codigo_de_alumno)
        except ValueError:                                                                                                      #****despues habran muchso "try" , es para cerciorarnos* que toda excepcion sea controlada y no salte un error
            print("Porfavor ingrese un entero.")

    elif opcion == "5":
        print("Seleccionó la opción Mensaje")
        try:
            ID_registro_EMISOR   = int(input("Ingrese el ID de registro del EMISOR: "))
            ID_registro_RECEPTOR = int(input("Ingrese el ID de registro del RECEPTOR: "))
            contenido_del_mensaje = input("Ingrese el mensaje: ")
            bool = buscar_ID(lista_de_alumnos, ID_registro_EMISOR)
            bool2 = buscar_ID(lista_de_alumnos,ID_registro_RECEPTOR)
            if bool != None and bool2 != None:
                lista_de_mensajes = mensaje(ID_registro_EMISOR, ID_registro_RECEPTOR, contenido_del_mensaje, lista_de_mensajes)
            else:
                print("Algun ID no se encontro.")
        except ValueError:
            print("Porfavor ingrese un entero.")

    elif opcion == "6":
        print("Seleccionó la opción Ver Historial")
        ver_historial(lista_de_mensajes, lista_de_alumnos)

    elif opcion == "7":
        guardar(lista_de_alumnos, lista_de_mensajes, ID)
        print("Finalizó el programa")                                                                                                              #acabop    IZI PE :v         estudialo bien pls
