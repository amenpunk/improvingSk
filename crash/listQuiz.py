filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [ x.replace(".hpp", ".h") for x in filenames]

# print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
def pig_latin(text):
    say = ""
    words = text.split()
    latin = []
    for word in words:
        latin.append( word[1:] + word[0] + "ay")
    return " ".join(latin)

# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    for code in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if code >= value:
                result += letter
                code -= value
            else:
                result += "-"
    return result

# print(octal_to_string(755)) # Should be rwxr-xr-x
# print(octal_to_string(644)) # Should be rw-r--r--
# print(octal_to_string(750)) # Should be rwxr-x---
# print(octal_to_string(600)) # Should be rw-------

def group_list(group, users):
    members = "{}: {}".format(group, ", ".join(users))
    return members

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"

def guest_list(guests):
    for name,age,profession in guests:
        string = "{} is {} years old and works as {}"
        print(string.format(name,age,profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
