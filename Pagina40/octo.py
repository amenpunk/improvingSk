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

piramide()
