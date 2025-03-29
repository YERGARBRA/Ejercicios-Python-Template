# coding=utf-8
__Author__="Yeray de la Cruz García Bravo"

def obtenerCalificacion(nota):
    if (nota > 10 or nota < 0):
        return "Incorrecta"
    elif (nota > 8):
        return "Sobresaliente"
    elif (nota > 6):
        return "Notable"
    elif (nota > 5):
        return "Bien"
    elif (nota > 4):
        return "Suficiente"
    elif (nota >= 3):
        return "Insuficiente"
    else:
        return "Muy deficiente"

# Programa principal
def main():
    n=int(input("Introduzca la nota: "));
    print('Calificación: '+ obtenerCalificacion(n));
if __name__== "__main__" :
   main()
