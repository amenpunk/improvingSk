import string
#cadenas en python

prefijo = "iuaoe"
sufijo = "put"

def cadP():
    for letra in prefijo:
        print (sufijo+letra)

## palindromo 
## las cadenas son inmutables

def palindromo(word):
    cont = len(word)
    reverse = ""
    x=0
    while cont != 0:
        reverse += word[cont-1]
        cont=cont-1
        x=x+1
    if word == reverse:
        print(word,"Es igual a",reverse,"Por lo tanto es un ","Palindromo")
    else:
        print(word,"No es igual a",reverse,"Por lo tanto no es un ","Palindromo")

#palindromo("reconocer")
#palindromo("Hola")

voc = ["hola","adios","aqui"]
num = range(0,20,2)
vacio = []
voc2 = ["hola","adios","aqui",[1,2,3.4]]

#print(voc , vacio, num, len(voc2))
#print("jaja" in voc2)

def newPar(ulti):
    for num in range(ulti):
        if num % 2 == 0:
            print(num ,"es par")
        else:
            print(num ,"es impar")

newPar(10)
