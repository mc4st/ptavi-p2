#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fich = open(sys.argv[1], "r")
lineas = fich.readlines()

calc = calcoohija.CalculadoraHija()

for linea in lineas:
    datos = linea.split(',')
    operacion = datos[0]
    if operacion == "suma":
        sum1 = calc.plus(int(datos[1]), int(datos[2]))
        sum2 = sum1
        print(sum1)
        for operandos in datos[3:]:
            sum2 = calc.plus(int(sum2), int(datos[???????]))
            print(sum2)
