#Pruebas de asignación
r = 5
num1 = r
num2 = 100


#Pruebas de operaciones aritméticas básicas
r = r - 1
suma = 2.7 + num1
resta = 5 - r
multiplicacion = suma * 20
division = multiplicacion / 5

#Pruebas de expresiones booleanas básicas
r == suma
num1 != num2
resta < 100
150.5 <= r
100 > resta
num2 >= 5.5

#Pruebas de formulas complejas del tipo c = a op ( b op d)
total = 20 * (30 + suma)
porcentaje = (num2 * 50) / 100

#Pruebas de encabezados de estructuras de control

#Estructura IF
edad = 21
if edad < 18:
    print("Es usted menor de edad")
else:
    print("Es usted mayor de edad")

#ESTRUCTURA WHILE
numero = 1
while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print ("La suma es " + str(suma))

#ESTRUCTURA FOR (DIFERENTES FORMAS)
print('Generar una lista del 0 al 4 y mostrarla por pantalla')
for i in range(5):
    print(i)
# Fin del bucle

print('Lista entre 10 y 20')
for j in range(10, 21):
    print(j)
# Fin del bucle

print('Lista de múltiplos de 3 hasta el 30 inclusive')
for multiploDeTres in range(3, 31, 3):
    print(multiploDeTres)
# Fin del bucle