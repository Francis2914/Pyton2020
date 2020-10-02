def menu():
    print('******MENU******')
    print('1.- Crear nombre de la lista')
    print('2.- Ingreso por teclado datos')
    print('3.- Busqueda en directorio')
    print('4.- Edito la lista')
    print('5.- Mostrar lista')
    print('6.- Salir')
    print()
 
def menu2():
    print('a.- Busqueda por nombre')
    print('b.- Busqueda por telefono')
    print('c.- Busqueda por direccion')
 
def menu3():
    print("Editar lista")
    print('1.- Eliminar un contacto')
    print('2.- Editar un contacto')
 
directorio = []
telefonos = {}
nombres = {}
direcciones = {}
apodos = {}
opcionmenu = 0
menu()
x=0
while opcionmenu != 6:
    opcionmenu = int(input("Inserta un numero para elegir una opcion: "))
    if opcionmenu == 1:
        print('Ingrese el nombre de la lista:')
        nombre_de_lista=input()
        menu()
 
 
    elif opcionmenu == 2:
        print("Agregar Nombre, telefono, direccion y apodo")
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        direccion = input("Direccion: ")
        apodo = input("Apodo: ")
        telefonos[nombre] = telefono
        nombres[telefono] = nombre
        direcciones[direccion] = nombre
        directorio.append([nombre, telefono, direccion, apodo])
        menu()
 
    elif opcionmenu == 3:
        print("Busqueda")
        menu2()
        opcionmenu2 = input("Inserta una letra para elegir una opcion: ")
        if opcionmenu2=="a":
            nombre = input("Nombre: ")
            if nombre in telefonos:
                print("El telefono es", telefonos[nombre])
            else:
                print(nombre, "no se encuentra")
 
        if opcionmenu2=="b":
            telefono = input("Telefono: ")
            if telefono in nombres:
                print("El Nombre es", nombres[telefono])
            else:
                print(telefono, "no se encuentra")
 
if opcionmenu2=="c":
            direccion = input("direccion: ")
            nombre=direcciones.get(direccion, '')
            if nombre:
                print('El nombre es: ', nombre)
            else:
                print('No hay registro para la dirección ', direccion)
        menu()
    elif opcionmenu == 4:
        menu3()
        opcionmenu3 = input("Inserta un numero para elegir una opcion: ")
        if opcionmenu3=="1":
            nombre = input("Nombre: ")
            index = None
            for i in range(len(directorio)):
                if directorio[i][0] == nombre:
                    index = i
                    break
            if index != None:
                del directorio[index]
                print('borrado')
            else:
                print(nombre, "no encontrado")
        elif opcionmenu3=="2":
            nombre = input("Nombre: ")
            # Editar - primero hay buscar el registro
            index = None
            for i in range(len(directorio)):
                if directorio[i][0] == nombre:
                    index = i
                    break
            if index != None:
                print('Omite aquellos campos que no quieras editar para conservar los datos')
                nombre = input('Nombre:')
                telefono = input('Telefono: ')
                direccion = input('Dirección')
                apodo = input('Apodo: ')
                directorio[index] = [
                        nombre if len(nombre) > 0 else directorio[index][0],
                        telefono if len(telefono) > 0 else directorio[index][1],
                        direccion if len(direccion) > 0 else directorio[index][2],
                        apodo if len(apodo) > 0 else directorio[index][3]
                ]
                print('Editado con exito!')
            else:
                print('El usuario no se encuentra en el directorio')
            menu()
        menu()
 
    elif opcionmenu == 5:
 
        print("\nNombre de la lista: ",nombre_de_lista)
        for e in directorio:
            print("\nLa lista es: ",directorio)
        menu()
 
 
    elif opcionmenu != 6:
        menu()
        