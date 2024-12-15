from package_biblioteca.config import *


def menu_cliente():
    print('Bienvenido a al menu de cliente')
    print('\nQue opcion desea realizar?')
    print('1 - Agregar nuevo Cliente')
    print('2 - Ver Clientes')
    print('3 - Buscar Cliente')
    print('4 - Volver al menu principal')
    print('5 - Salir')

    opc = input('\nSu opcion: ')

    if opc == '1':

        agregar_cliente(cliente)
        menu_cliente()

    elif opc == '2':

        ver_cliente(cliente)
        menu_cliente()

    elif opc == '3':

        buscar_cliente(cliente)
        menu_cliente()

    elif opc == '4':

        print("Salio del menu cliente.\n")

    elif opc == '5':

        exit()

    else:
        print('\n\nNo ingreso una opcion valida!!!!!\n\n')


def agregar_cliente(clien):
    nuevo = input('agregar nombre y apellido del nuevo cliente\n')
    clien.append(nuevo)
    return clien


def ver_cliente(clien):
    print(clien)


def buscar_cliente(clien):
    nombre = input("agregar el primer nombre y primer apellido del cliente que desea buscar\n")

    if nombre in clien:
        print(nombre, "se encuentra en la lista de clientes\n")

    else:
        print(nombre, "no se encuentra en la lista de clientes\n")
