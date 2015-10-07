#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

if __name__ == "__main__":

    fich = open(sys.argv[1], "r")
    lineas = fich.readlines()
    calc = calcoohija.CalculadoraHija()

    for linea in lineas:
        datos = linea.split(',')
        operacion = datos[0]
        diccoperandos = {"suma": calc.plus, "resta": calc.minus, 
                         "multiplica": calc.mult, "divide": calc.div}
        if operacion in ["suma", "resta", "multiplica", "divide"]:
            solucion = datos[1]
            for operandos in datos[2:]:
                solucion = diccoperandos[operacion](solucion, operandos)
            print(solucion)
