import re

filename = "Ejemplos.py"
textFile = open(filename, "r")
regex1 = "[a-z]+\d*[-|_]*[a-zA-Z]*\s=\s\d*\w*$"
lista_temp1 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex1, linea)
    if len(x) > 0:
        lista_temp1.append(x)

filename = "Ejemplos.py"
textFile = open(filename, "r")
regex2 = "[a-z]+\d*[-|_]*[a-zA-Z]*\s=\s[a-zA-Z|\d|\d.]*\s[+|\-|*|/]\s[a-zA-z|\d|\d.]*$"
lista_temp2 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex2, linea)
    if len(x) > 0:
        lista_temp2.append(x)

filename = "Ejemplos.py"
textFile = open(filename, "r")
regex3 = "([A-za-z|\d|\d.]*\s([>=]{2}|[<=]{2}|[!=]{2}|[>]|[<])\s[A-za-z|\d|\d.]*)"
lista_temp3 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex3, linea)
    if len(x) > 0:
        lista_temp3.append(x)

filename = "Ejemplos.py"
textFile = open(filename, "r")
regex4 = "[\w]*\s=\s[\w|\d|\d.]*\s[+|\-|*|/]\s[()|\d|\d.|\w]*\s[+|\-|*|]\s[()|\d|\d.|\w]*|[A-Za-z]*\s=\s[()|\d|\d.|\w]*\s[+|\-|*|/]*\s[()|\d|\d.|\w]*\s[+|\-|*|/]*\s[()|\d|\d.|\w]"
lista_temp4 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex4, linea)
    if len(x) > 0:
        lista_temp4.append(x)

filename = "Ejemplos.py"
textFile = open(filename, "r")
regex5 = "(if\s[\w]*\s([>=]{2}|[<=]{2}|[!=]{2}|[>]|[<])\s[\w]*:|while\s[\w]*\s([>=]{2}|[<=]{2}|[!=]{2}|[>]|[<])\s[\w]*:|for\s[\w]*\sin\s[\w]*:|for\s[\w]*\sin\s[\w]*[()|\d|,\s]*:)"
lista_temp5 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex5, linea)
    if len(x) > 0:
        lista_temp5.append(x)

print("-------------------------EJERCICIO 1--------------------------")
print("Las sentencias de asignación encontradas en el archivo son:")
print(str(lista_temp1)+"\n")
print("-------------------------EJERCICIO 2--------------------------")
print("Las operaciones aritméticas básicas encontradas en el archivo son:")
print(str(lista_temp2)+"\n")
print("-------------------------EJERCICIO 3--------------------------")
print("Las expresiones booleanas básicas encontradas en el archivo son:")
print(str(lista_temp3)+"\n")
print("-------------------------EJERCICIO 4--------------------------")
print("Las formulas complejas del tipo c = a op ( b op d) encontradas en el archivo son:")
print(str(lista_temp4)+"\n")
print("-------------------------EJERCICIO 5--------------------------")
print("Los encabezados de estructuras de control encontrados en el archivo son:")
print(str(lista_temp5)+"\n")
