gundam = "    barbatos lopus rex    "
numeric = '2131231'
gg = "jaja memes xd python"

def printStrings():
    print(gundam.strip())
    print(gundam.lstrip())
    print(gundam.rstrip())
    print(gundam.lower())
    print(gundam.upper())
    print(gundam.count("a"))
    print(numeric.isnumeric())
    print("-".join(numeric))
    print(gg.split())


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("local area network")) # Should be: LAN

def format():
    print("Hola {} quiero decir {}".format(gundam.strip(), gundam.strip().split()[0]))
    print("Hola {gun} tu numero es {num}".format(gun=gundam.strip(), num=numeric))

#format()

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)


#print(student_grade("Jesse", 85))

def formatStyle():
    price = 7.5
    with_tax = price * 1.09
    print("Base price: ${:.2f}. With Tax: ${:.2f}.".format(price,with_tax))

#formatStyle()
