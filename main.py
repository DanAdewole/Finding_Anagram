# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, mode='r') as file:
        info = file.read()
    
    return info


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_count = {}
    words_in_text = text.split()

    for word in words_in_text:
        occurrence = words_in_text.count(word)
        word_count[word] = occurrence

    return word_count


print(count_words())

