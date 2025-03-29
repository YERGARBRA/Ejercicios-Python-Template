# This Python file uses the following encoding: utf-8
__Author__="Jose Gaspar Sanchez Garcia"
import os, sys

# Ejemplo de fichero de pruebas pytest
# Autor: José Gaspar Sánchez García

import ejercicio3 as t

def test_obtenerCalificacion():
    assert t.obtenerCalificacion(0) == "Muy deficiente"
    assert t.obtenerCalificacion(1) == "Muy deficiente"
    assert t.obtenerCalificacion(2) == "Muy deficiente"
    assert t.obtenerCalificacion(3) == "Insuficiente"
    assert t.obtenerCalificacion(4) == "Insuficiente"
    assert t.obtenerCalificacion(5) == "Suficiente"
    assert t.obtenerCalificacion(6) == "Bien"
    assert t.obtenerCalificacion(7) == "Notable"
    assert t.obtenerCalificacion(8) == "Notable"
    assert t.obtenerCalificacion(9) == "Sobresaliente"
    assert t.obtenerCalificacion(10) == "Sobresaliente"
    assert t.obtenerCalificacion(-1) == "Incorrecta"
    assert t.obtenerCalificacion(11) == "Incorrecta"
