from package_biblioteca.config import *


def menu_prestamos():
    print('\nBienvenido  al menu de libros prestados!')
    print('\nQue opcion desea realizar?')
    print('1 - Prestar libro')
    print('2 - Prestar audiolibro')
    print('3 - Visualizacion de articulos prestados')
    print('4 - Articulos devueltos')
    print('5 - volver al menu principal ')
    print('6 - salir')

    opc = input('\nSu opcion: ')

    if opc == '1':

        prestar_libro(libros, cliente, prestamol)
        menu_prestamos()

    elif opc == '2':

        prestar_audiolibro(audiolibros, cliente, prestamol)
        menu_prestamos()

    elif opc == '3':

        print(prestamol)
        menu_prestamos()

    elif opc == '4':

        devolver_articulo(libros, audiolibros, prestamol)
        menu_prestamos()

    elif opc == '5':

        print("Salio del menu prestamo.\n")

    elif opc == '6':

        exit()

    else:
        print("Esta no es una opcion.\nIngrese nuvevamente la opcion.")


prestamol = {}


def prestar_libro(book, perso, presta):
    buscarl = input("Digite el libro que desea prestar:")

    buscarp = input("Digite la persona que desea el libro")

    if buscarp in perso:

        if buscarl in book:
            book.pop(buscarl)
            print(f"Libro prestado a {buscarp}")
            presta.update({buscarl: 'Libro prestado a ' + buscarp})
            print("Prestamo exitoso")
            return presta

        else:
            print("El libro no esta en la biblioteca")

    else:
        print(buscarp, "no se encuentra en la lista de clientes\n")


def prestar_audiolibro(book, perso, presta):
    buscarl = input("Digite el audiolibro que desea prestar:")

    buscarp = input("Digite la persona que desea el libro")

    if buscarp in perso:

        if buscarl in book:
            book.pop(buscarl)
            print(f"audioLibro prestado a {buscarp}")
            presta.update({buscarl: 'Audiolibro prestado a ' + buscarp})
            print("Prestamo exitoso")
            return presta

        else:
            print("El libro no esta en la biblioteca")

    else:
        print(buscarp, "no se encuentra en la lista de clientes\n")


def devolver_articulo(book, audio, pret):
    print('Que tipo de articulo desea devolver?')
    print('\nQue opcion desea elegir?')
    print('1 - Libro')
    print('2 - Audiolibro')

    opcion = input('\nSu opcion: ')

    if opcion == "1":

        k = input("Introduce el titulo del libro: ")
        v = input("Introduce el nombre del autor del libro y fecha de publicacion: ")
        book.update({k: v})
        pret.pop(k)
        print("El libro ha sido devuelto exitosamente a la biblioteca")

    elif opcion == "2":

        k = input("Introduce el titulo del audiolibro: ")
        v = input("Introduce el nombre del autor del audiolibro y fecha de publicacion: ")
        audio.update({k: v})
        pret.pop(k)
        print("El audiolibro ha sido devuelto exitosamente a la biblioteca")

    else:
        print("Esta no es una opcion.\nIngrese nuvevamente la opcion.")
