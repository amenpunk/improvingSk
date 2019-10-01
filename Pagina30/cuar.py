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

table(2,2)
#default argument:

def calcIva(num,por=1):
    return num*por

#print(calcIva(2))
#print(calcIva(2,2))
#print(calcIva(2,por=4))
#print(calcIva(2))

## orden de los parametros
def sumar(num1,num2):
    print (num1)
    print (num2)
    print (num1+num2)

#sumar(num2=20,num1=10)

## multiples parametros

def listaSum(lis):
    sum=0
    for i in lis:
        sum=sum+i
    return sum 

lis = range(6)
#print(listaSum(lis))

## multiple parametros

def multiPar(**letra):
    print(letra['parm0'] +letra['parm1'] +letra['parm2'] +letra['parm3'] )

multiPar(parm0="h",parm1="o",parm2="l",parm3="a")

