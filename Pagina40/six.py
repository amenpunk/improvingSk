import math

## condicional semantica

def betEdad(num):
    if 0 < num < 18:
        print("Menor de edad")
    elif 19 < num < 40:
        print("Adulto")
    else:
        print("Adulto Mayor")

#nume = int(input("Ingresa tu edad: "))
#betEdad(nume)

def recursiv(n):
    if n == 0:
        print("BOOOM!")
    else:
        print(n)
        recursiv(n-1)

#recursiv(10)

''' recursividad infinita

def bucle():
    bucle()

bucle()
'''

def distancia(x1,y1,x2,y2):
    p1 = (x2-x1)**2
    p2 = (y2-y1)**2
    return math.sqrt(p1+p2)

def recWhile(n):
    while(n > 0):
        print(n)
        n=n-1
    print("BOOM!");

#var = int(input("A donde quiere contar?: "))
#recWhile(var)
def logTab():
    x = 1.0
    while(x <10.0):
        print (x ,'\t', math.log(x))
        x = x+1.0

#logTab()

def subNetHost(): 
    n = 30
    cont=2
    while(n>16):
        print("/",n,'\t',pow(2,cont))
        cont=cont+1
        n=n-1


subNetHost()
