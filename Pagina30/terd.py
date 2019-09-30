import math

minu = 47
hora = 60.0

frac = minu/int(hora)

## Composición de tipos
#print(type(hora))
#print(type(minu))
#print(int(math.sin(frac)))
#print(math.pi)

x = math.exp(math.log(10.0))
print(x)

def primerFuncion (nom,edad):
    print("Hola "+nom," Tienes ",edad," años")
        #val = 2
        #print("en dos años vas a tener", edad*2)
    val = 2
    print("en dos años vas a tener", edad+2)
    
primerFuncion("Juan",20)

