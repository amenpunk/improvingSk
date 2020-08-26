def format_address(address_string):
    strings = address_string.split()
    streat = []
    house = ""
    for char in strings:
        if char.isnumeric():
            house = char
        else:
            streat.append(char)
    return "house number {} on street named {}".format(str(house), " ".join(streat))

# print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"jj

def highlight_word(sentence, word):
    return  " ".join([ w.upper() if word in w else w for w in sentence.split()])

# print(highlight_word("Shhh, don't be so loud!", "loud"))

def combine_lists(list1, list2):
    reverse = list2[::-1]
    new_list = list1 + reverse
    print(new_list)
    return new_list

#Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
#Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#print(combine_lists(Jamies_list, Drews_list))

def squares(start, end):
    return [ x * x for x in range(start,end + 1) ]


# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def car_listing(car_prices):
    result = ""
    for name, price in car_prices.items():
        result += "{} costs {} dollars".format(name,str(price)) + "\n"
    return result

# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


def combine_guests(guests1, guests2):
    guests2.update(guests1)
    return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
# print(combine_guests(Rorys_guests, Taylors_guests))

def count_letters(text):
    result = {}
    for char in text:
        if char.isalpha():
            if not char.lower() in result:
                result[char.lower()] = 1
            else:
                result[char.lower()] += 1
    return result



print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
