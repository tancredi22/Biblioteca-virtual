from paquete.funcion_matematica import *
from paquete.funcion_avanzada import *


def menu_calculdaora():
    while True:

        vari = input("\nintroduce el numero de la operacion que quieres realizar:\n 1) Suma \n"
                     " 2) Resta\n 3) Multiplicacion\n 4) Division\n 5) Poteciacion \n "
                     "6) radicacion\n 7) area de un cuadrado\n"
                     " 8) area de un triangulo\n 9) area de un circulo\n 10) Profundidad de un canal\n"
                     " 11) Salir calculadora \n")

        if vari == "1":
            suma()
        elif vari == "2":
            resta()
        elif vari == "3":
            multiplicacion()
        elif vari == "4":
            division()
        elif vari == "5":
            poteciancion()
        elif vari == "6":
            radicacion()
        elif vari == "7":
            area_cuadrado()
        elif vari == "8":
            area_triangulo()
        elif vari == "9":
            area_circulo()
        elif vari == "10":
            profundidad_de_un_canal()
        elif vari == "11":
            exit()
        else:
            print("Esta no es una opcion para una operacion matematica propuesta.\nIngrese nuvevamente los numeros.")
