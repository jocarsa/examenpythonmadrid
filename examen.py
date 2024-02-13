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
    # Si ha elegido buscar, muestrame solo las entradas que coincidan
    elif opcion == "2":
        print("Buscamos un registro")
    # Si ha elegido insertar, pregunta los datos e inserta
    elif opcion == "3":
        print("Insertamos un registro")
        nombre = input("Indica el nombre del cliente: ")
        email = input("Indica el email del cliente: ")
        telefono = input("Indica el telefono del cliente: ")
    # Si ha elegido actualizar, pregunta cual se va a actualizar, pregunta datos, y reemplaza
    elif opcion == "4":
        print("Actualizamos un registro")
    # Si ha elegido eliminar, pregunta criterio y elimina
    elif opcion == "5":
        print("Eliminamos un registro")
    # Si ha elegido salir, sal
    elif opcion == "6":
        print("Salimos")
        sys.exit()
menu()
