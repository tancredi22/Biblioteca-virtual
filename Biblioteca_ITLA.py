from package_biblioteca.catalogo import *
from package_biblioteca.cliente import *
from Calculadora_extensa import *

print('------------------------------')
print(f'-- Biblioteca Itla virtual --')
print('------------------------------')


while True:
    print('Bienvenido a la libreria virtual ITLA!')
    print('\nQue opcion desea elegir?')
    print('1 - Catalogo')
    print('2 - Clientes')
    print('3 - Salir')
    print('4- calculadora')

    opcion = input('\nSu opcion: ')

    if opcion == "1":

        menu_catalogo()

    elif opcion == "2":

        menu_cliente()

    elif opcion == "3":

        exit()

    elif opcion == "4":

        menu_calculdaora()

    else:
        print("Esta no es una opcion.\nIngrese nuvevamente la opcion.")



