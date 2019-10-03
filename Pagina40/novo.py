import string
#listas anidadas 
lista = [0,1,[2,4,5],6]

def toSix(lista):
    cont = 0
    for x in lista:
        if cont == 2:
            continue
        else:
            print(lista[x])
        cont=cont+1


#toSix(lista)

matix = [[1,2,3],[4,5,6],[7,8,9]]
#print(matix)
var = "h o y e s u n h e r m o s o d i a"
sp = str.split(var)
print(sp)
