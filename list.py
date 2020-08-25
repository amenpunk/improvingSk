def get_word(sentence, n):
    # Only proceed if n is positive 
        if n > 0:
            words = sentence.split()
                # Only proceed if n is not more than the number of words 
            if n <= len(words):
                return words[n - 1]
        return("")

def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0
    # Iterate through the list
    for e in elements:
        # Does this element belong in the resulting list?
        if i % 2 == 0:
            new_list.append(e)
        i = i + 1
    return new_list

print(skip_elements([])) # Should be []

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format( size/ 1024))

#print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46

def indexes():
    l = ["ab", "ac", "af"]
    print(enumerate(l))
    for i,a in enumerate(l):
        print("{} - {}".format(i, a))


def full_emails(people):
    res = []
    for email, name in people:
        res.append("{} <{}>".format(name, email))

    return res

persons = [('gg@gg.com', 'gg'),('ff@ff.com', 'ff')]

def odd_numbers(n):
    return [x*2 for x in range(1,n + 1) if x % 2 !=0 ]

#print(odd_numbers(5))  # Should print [1, 3, 5]
#print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
