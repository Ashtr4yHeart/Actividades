
def sumatoria():
    #Entrada del usuario
    x = int(input("Introduce un número "))
    y = int(input(f"introduce el número que le quieres agregar "))
    print(f"Resultado {x + y}")
    #Llamada a la función
    sumatoria(x, y)


def sustracción():
    #Entrada del usuario
    a = int(input("Introduzca un número "))
    b = int(input("Introduzca el número que quiere restar "))
    print(f"Resultado {a - b}")
    #Llamada a la función
    sustracción(a, b)


def multiplicación():
    #Entrada del usuario
    n = int(input("Introduzca un número "))
    m = int(input("Introduzca el número que quiere multiplicar "))
    print(f"Resultado {n + m}")
    #Llamada a la función
    multiplicación(n, m)


def división():
    #Entrada del usuario
    c = int(input("Introduce un divisor "))
    d = int(input("Introduce un dividendo "))
    print(f"Resultado {c / d}") 
    #Llamada a la función
    división(c, d)



def divisionresiduo():
    #Entrada del usuario 
    p = int(input("Introduce un divisor "))
    q = int(input("Introduce un dividendo "))
    print(f"Resultado {p % q}") 
    #Llamada a la función
    divisionresiduo(p, q)

#Código de opciones
def operaciones():
    while True:
        print("Seleccione una operación: ")
        print("sumatoria")
        print("sustracción")
        print("multiplicación")
        print("división")
        print("divisionresiduo")

    #Entrada del usuario
        operación = input("")

        if operación == "sumatoria":
            sumatoria()
        elif operación == "sustracción":
            sustracción()
        elif operación == "multiplicación":
            multiplicación()
        elif operación == "división":
            división()
        elif operación == "divisionresiduo":
            divisionresiduo()
        else:
            print(" ")
#Llamada de función de operaciones
operaciones()

