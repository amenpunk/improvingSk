import random

def isPar(num):
    if num%2 <= 0:
        print(num, "Es par")
    else:
        print(num, "No es par")


def listaPar(num):
    for i in num:
        if num[i]%2 <= 0:
            print(num[i], "Es par")
        else:
            print(num[i], "No es par")

#isPar(10)
lis = range(10)
#listaPar(lis)


### -- condiciones anidadas
gen = ["Breakcore","DrillAndBass","SmashCore","Hartek","IDM"]

def douCont(gen):
    rand = random.choice(gen)
    if rand == "Breakcore":
        print(rand,"nice taste")
    else:
        if rand == "IDM":
            print(rand,"Oh a men of Culture")
        else:
            print(rand,"is ok")

#douCont(gen)

