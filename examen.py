import sys

def menu():
    # Primero mostramos el menu
    print("Programa de empresa (c) 2024 Jose Vicente Carratala")
    print("Escoge una opcion de las siguientes:")
    print("1.-Listar")
    print("2.-Buscar")
    print("3.-Insertar")
    print("4.-Actualizar")
    print("5.-Eliminar")
    print("6.-Salir")   
    # Atrapamos la opción que ha seleccionado el usuario
    opcion = input("Opción selecionada: ")
    
    # Si ha elegido listar, muestrame el contenido del archivo de datos
    if opcion == "1":
        print("Listamos los registros")
        # Leo el archivo y muestro el contenido en pantalla
        archivo = open("clientes.txt",'r')
        for linea in archivo:
            print(linea)
        archivo.close()
    # Si ha elegido buscar, muestrame solo las entradas que coincidan
    elif opcion == "2":
        print("Buscamos un registro")
        criterio = input("Indica a quién buscas: ")
        archivo = open("clientes.txt",'r')
        for linea in archivo:
            if criterio in linea:
                print(linea)
        archivo.close()
    # Si ha elegido insertar, pregunta los datos e inserta
    elif opcion == "3":
        # Primero recogemos los datos
        print("Insertamos un registro")
        nombre = input("Indica el nombre del cliente: ")
        email = input("Indica el email del cliente: ")
        telefono = input("Indica el telefono del cliente: ")
        # Ahora guardamos los datos en el archivo
        archivo = open("clientes.txt",'a')
        archivo.write(nombre+","+email+","+telefono+",\n")
        archivo.close()
    # Si ha elegido actualizar, pregunta cual se va a actualizar, pregunta datos, y reemplaza
    elif opcion == "4":
        print("Actualizamos un registro")
        contenido = ""
        criterio = input("Introduce el cliente que quieras cambiar")
        nombre = input("Indica el nombre del cliente a actualizar: ")
        email = input("Indica el email del cliente a actualizar: ")
        telefono = input("Indica el telefono del cliente a actualizar: ")
        # Primero leemos y volcamos el contenido:
        archivo = open("clientes.txt",'r')
        for linea in archivo:
            if not criterio in linea:
                contenido += linea
            else:
                contenido += nombre+","+email+","+telefono+",\n" 
        archivo.close()
        # Ahora escribimos el archivo
        archivo = open("clientes.txt",'w')
        archivo.write(contenido)
        archivo.close()
    # Si ha elegido eliminar, pregunta criterio y elimina
    elif opcion == "5":
        print("Eliminamos un registro")
        criterio = input("Introduce a quién deseas eliminar: ")
        contenido = ""
        # Leo el archivo y evito ese registro
        archivo = open("clientes.txt",'r')
        for linea in archivo:
            if not criterio in linea:
                contenido += linea
        archivo.close()
        # Ahora escribo el archivo con el contenido filtrado
        archivo = open("clientes.txt",'w')
        archivo.write(contenido)
        archivo.close()
    # Si ha elegido salir, sal
    elif opcion == "6":
        print("Salimos")
        sys.exit()
    menu()
menu()
