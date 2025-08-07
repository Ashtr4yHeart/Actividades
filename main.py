numero = 1 
#Bucle while como en el diagrama Rombo
while numero < 21:
    #Estrcuturas de control condicional 
    if numero % 15 == 0:
     print ("FizzBuzz")
    elif numero % 3 == 0: 
     print ("Fizz")
    elif numero % 5 == 0:
      print("Buzz")
    else: print (numero)
    