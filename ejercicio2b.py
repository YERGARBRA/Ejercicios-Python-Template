# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.
__Author__="Yeray de la Cruz García Bravo"
# Implemente función esMayorEdad(e)

def esMayorEdad(edad):
    if (edad >= 18):
        return True
    else:
        return False

# Programa principal
def main():
    nombre=input("Escribe tu nombre: ");
    edad=int(input("Escribe tu edad: "));
    
    if(esMayorEdad(edad)):
        print(nombre + " es mayor de edad.")
    else:
        print(nombre + " es menor de edad.")
    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

if __name__== "__main__" :
   main()