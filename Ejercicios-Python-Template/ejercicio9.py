# coding=utf-8
__Author__="José Gaspar Sánchez García"

def suma(x,y) :
    x = x+y
    return x

def resta(x,y) :
    x = x - y
    return x

def multiplica(x,y) :
    x = x * y
    return x

def divide(x,y) :
    if(y != 0):
        y = x/y
        return y
    else:
        return "Error, no se puede dividir entre 0, deberías saberlo :("

# Función que crea el menú de la aplicacion.

def menuApp() :
    print("MENU CALCULADORA")
    opcion =-1

    while opcion !=0 :
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion=int(input("Introduzca opción: "))

        if opcion == 1:
            s1 = int(input("Introduzca el primer sumando: "))
            s2 = int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.".format(s1, s2, suma(s1, s2)))
        elif opcion == 2:
            minuendo = int(input("Introduzca el minuendo: "))
            sustraendo = int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.".format(minuendo, sustraendo, resta(minuendo, sustraendo)))
        elif opcion == 3:
            m1 = int(input("Introduzca el primer factor: "))
            m2 = int(input("Introduzca el segundo factor: "))
            print("La multiplicación de {0} * {1} = {2}.".format(m1, m2, multiplica(m1, m2)))
        elif opcion == 4:
            d1 = int(input("Introduzca el dividendo: "))
            d2 = int(input("Introduzca el divisor: "))
            print("La división de {0} / {1} = {2}.".format(d1, d2, divide(d1, d2)))
        elif opcion == 0:
            print("Saliendo del programa...")
        else:
            print("Opción incorrecta, introduzca una opción válida, si puede ser de los números DEL MENU")
            
# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()
