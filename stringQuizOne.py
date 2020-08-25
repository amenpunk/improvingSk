def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the 
		# end of one string, and to the front
		# of the other string. 
                if letter != " ":
                    new_string = new_string + letter.lower()
                    reverse_string= letter.lower() + reverse_string
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

#print(is_palindrome("Never Odd or Even")) # Should be True


def convert_distance(miles):
    km = miles * 1.6
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result

#print(convert_distance(12)) # Should be: 12 miles equals 19.2 km

def nametag(first_name, last_name):
    return("{} {}.".format(first_name, last_name[0]))

#print(nametag("Jane", "Smith")) 
# Should display "Jane S." 

def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence 
        if sentence.endswith(old):
            # Using i as the slicing index, combine the part
            # of the sentence up to the matched string at the 
            # end with the new string
            i = len(old)
            new_sentence = sentence[0:len(sentence) - i] + new
            return new_sentence

        # Return the original sentence if there is no match 
        return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
