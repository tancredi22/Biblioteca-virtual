def suma():
    a = input("ingrese un numero: ")
    x = a.isdigit()

    if x == 0:
        print("El caracter ingresado no es un numero ")
        while x == 0:
            a = input("ingrese un numero nuevamente: ")
            x = a.isdigit()

    b = input("ingrese un numero: ")
    y = b.isdigit()

    if y == 0:
        print("El caracter ingresado no es un numero ")
        while y == 0:
            b = input("ingrese un numero nuevamente: ")
            y = b.isdigit()
    n1 = int(a)
    n2 = int(b)
    print("\t", n1 + n2)


def multiplicacion():
    a = input("ingrese un numero: ")
    x = a.isdigit()

    if x == 0:
        print("El caracter ingresado no es un numero ")
        while x == 0:
            a = input("ingrese un numero nuevamente: ")
            x = a.isdigit()

    b = input("ingrese un numero: ")
    y = b.isdigit()

    if y == 0:
        print("El caracter ingresado no es un numero ")
        while y == 0:
            b = input("ingrese un numero nuevamente: ")
            y = b.isdigit()
    n1 = int(a)
    n2 = int(b)
    print("\t", n1 * n2)


def resta():
    a = input("ingrese un numero: ")
    x = a.isdigit()

    if x == 0:
        print("El caracter ingresado no es un numero ")
        while x == 0:
            a = input("ingrese un numero nuevamente: ")
            x = a.isdigit()

    b = input("ingrese un numero: ")
    y = b.isdigit()

    if y == 0:
        print("El caracter ingresado no es un numero ")
        while y == 0:
            b = input("ingrese un numero nuevamente: ")
            y = b.isdigit()
    n1 = int(a)
    n2 = int(b)
    print("\t", n1 - n2)


def division():
    a = input("ingrese un numero: ")
    x = a.isdigit()

    if x == 0:
        print("El caracter ingresado no es un numero ")
        while x == 0:
            a = input("ingrese un numero nuevamente: ")
            x = a.isdigit()

    b = input("ingrese un numero: ")
    y = b.isdigit()

    if y == 0:
        print("El caracter ingresado no es un numero ")
        while y == 0:
            b = input("ingrese un numero nuevamente: ")
            y = b.isdigit()
    n1 = int(a)
    n2 = int(b)
    print("\t", n1 / n2)
