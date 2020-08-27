file_contents = "International donations are gratefully accepted, but we cannot make any make make$ m#a$#k$$$$e"
#file_contents = "International donations are gratefully accepted, but we cannot make any statements concerning tax treatment of donations received from outside the United States. U.S. laws alone swamp our small staff.  Please check the Project Gutenberg Web pages for current donation methods and addresses. Donations are accepted in a number of other ways including checks, online payments and credit card donations. To donate, please visit: www.gutenberg.org/donate Section 5. General Information About Project Gutenberg-tm electronic works.  Professor Michael S. Hart was the originator of the Project Gutenberg-tm concept of a library of electronic works that could be freely shared with anyone. For forty years, he produced and distributed Project Gutenberg-tm eBooks with only a loose network of volunteer support.  Project Gutenberg-tm eBooks are often created from several printed editions, all of which are confirmed as not protected by copyright in the U.S. unless a copyright notice is included. Thus, we do not necessarily keep eBooks in compliance with any particular paper edition"
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

def test(file_contents):
    words = {}
    pu = []
    for word in file_contents.split():
        clean_word = ""

        for w in word.lower():
            if not w in punctuations:
                clean_word += w
        word = clean_word

        if word.isalpha() and  not word in uninteresting_words:
            if not word in words:
                words[word] = 1
            else:
                words[word] += 1

    return words


print(test(file_contents))
