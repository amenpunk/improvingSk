f = [1,2,3,4]
p = [5,6,7,8,9,10]
k = (f + p)

#print(f*2)
#porciones


def piramide():
    cont=len(k)
    tot = int(cont)
    while tot != 0:
        print(k[0:tot])
        tot=tot-1

## mutar listas

f[3] = -4
p[3:5] = []
p[4:5] = [11,12]

k = (f + p)
del k[len(k)-1]
del k[5:len(k)]

#piramide()
d = "iguas"
b = "igual"

def idTest():
    if id(d) == id(b):
        print("MISMO ID")
    else:
        print("DIFERENTE ID")
    #print(id(d), id(b))

# referencias entre variables
a = [1,2,3]
# asignacion del alias
b = a
b[0] = "cambio"
#print(a)

def clonarLista(a,b):
    b[len(b):] = a[:]

a = [9,8,7]
b = [0,1]

clonarLista(a,b)
print("desde b",b)
