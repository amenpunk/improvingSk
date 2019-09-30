import math

def raizCuadrada(num):
    var = math.sqrt(num)
    return var

def noIdent(saludo):
    print("hola", saludo)


print(raizCuadrada(3.52))
#noIdent("mundo")

#argumentos 

def table(n,y):
   print(n*y) 

#table(2,2)
#default argument:

def calcIva(num,por=1):
    return num*por

#print(calcIva(2))
#print(calcIva(2,2))
print(calcIva(2,por=4))
print(calcIva(2))



