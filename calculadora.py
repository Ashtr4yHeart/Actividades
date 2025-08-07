def sumatoria(x, y):
    suma = x + y 
    print("Resultado ", suma)
#Entrada del usuario
x = int(input("Introduce un número "))
y = int(input("introduce el número que le quieres agregar "))
#Llamada a la función
sumatoria(x, y)


def sustracción(a, b):
    resta = a - b
    print("Resultado ", resta)
#Entrada del usuario
a = int(input("Introduzca un número "))
b = int(input("Introduzca el número que quiere restar "))
#Llamada a la función
sustracción(a, b)


def multiplicación(n, m):
    producto = n * m
    print("Resultado ", producto)
#Entrada del usuario
n = int(input("Introduzca un número "))
m = int(input("Introduzca el número que quiere multiplicar "))
#Llamada a la función
multiplicación(n, m)


def división(c, d):
    cociente = c / d 
    print("Resultado ", cociente)
#Entrada del usuario
c = int(input("Introduce un divisor "))
d = int(input("Introduce un dividendo "))
#Llamada a la función
división(c, d)



def divisionresiduo(p , q):
    residuo = p % q 
    print("Módulo ", residuo)
#Entrada del usuario 
p = int(input("Introduce un divisor "))
q = int(input("Introduce un dividendo "))
#Llamada a la función
divisionresiduo(p, q)