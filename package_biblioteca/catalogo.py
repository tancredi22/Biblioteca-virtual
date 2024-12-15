from package_biblioteca.prestamos_libros import *
from package_biblioteca.config import *


def menu_catalogo():
    print('\nBienvenido a al menu del catalogo!')
    print('\nQue opcion desea realizar?')
    print('1 - Mostrar Libros')
    print('2 - Mostrar Audiolibros')
    print('3 - Mostrar catalogo completo')
    print('4 - Agregar Libro')
    print('5 - Agregar Audiolibro')
    print('6 - Volver al menu principal')
    print('7 - Seccion de prestamos de libros')
    print('8 - Salir')

    opc = input('\nSu opcion: ')

    if opc == '1':

        mostrar_libros(libros)
        menu_catalogo()

    elif opc == '2':

        mostrar_audilibro(audiolibros)
        menu_catalogo()

    elif opc == '3':

        mostrar_catalogo_completo(libros, audiolibros)
        menu_catalogo()

    elif opc == '4':

        agregar_book(libros)
        menu_catalogo()

    elif opc == '5':

        agregar_audibook(audiolibros)
        menu_catalogo()

    elif opc == '6':

        print("Salio del menu catalogo.\n")

    elif opc == '7':

        menu_prestamos()

    elif opc == '8':

        exit()

    else:
        print('\n\nNo ingreso una opcion valida!!!!!\n\n')


def mostrar_libros(book):
    print("Titulo del libro y fecha de publicacion:\n")
    for x in book:
        print(x, ",", book[x])


def mostrar_audilibro(book):
    print("Titulo del audiolibro y fecha de publicacion:\n")
    for x in book:
        print(x, ",", book[x])


def mostrar_catalogo_completo(book, book2):
    print("Titulo del libro y fecha de publicacion:\n")
    for x in book:
        print(x, ",", book[x])

    print("\nTitulo del audiolibro y fecha de publicacion:\n")
    for x in book2:
        print(x, ",", book2[x])


def agregar_book(book):
    k = input("Introduce el titulo del libro: ")
    v = input("Introduce el nombre del autor del libro y fecha de publicacion: ")
    book.update({k: v})
    print(book)
    return book


def agregar_audibook(book):
    k = input("Introduce el titulo del audiolibro: ")
    v = input("Introduce el nombre del autor del audiolibro y fecha de publicacion: ")
    book.update({k: v})
    print(book)
    return book
