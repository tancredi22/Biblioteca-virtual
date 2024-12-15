def poteciancion():
    a = int(input("ingrese numero base:"))
    n = int(input("ingrese numero exponente para la base:"))
    print("resultado de la operacion=", a ** n)


def radicacion():
    a = float(input("ingrese numero radicando:"))
    n = float(input("ingrese indice para la raiz:"))
    nr = 1 / n
    print("resultado de la operacion=", a ** nr)


def area_cuadrado():
    b = int(input("ingrese el valor de la base del cuadrado : "))
    h = int(input("ingrese el valor de la altura del cuadrado : "))
    area = b * h
    print(area, "metros cuadrado")


def area_triangulo():
    b = int(input("ingrese el valor de la base del triangulo : "))
    h = int(input("ingrese el valor de la altura del triangulo : "))
    area = (b * h) / 2
    print(area, "metros cuadrado")


def area_circulo():
    r = int(input("ingrese el valor del radio del circulo : "))
    area = 3.1416 * (r ** 2)
    print(area, "metros cuadrado")


def profundidad_de_un_canal():
    q = int(input("ingrese el valor del caudal: "))
    b = int(input("ingrese la base: "))
    grave = 9.81
    raid = 1 / 3
    yc = ((q ** 2) / ((b ** 2) * grave)) ** raid
    print(yc, "metros")
