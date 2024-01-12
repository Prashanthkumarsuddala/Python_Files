def reverse_words(words):
    a=word.split(" ")
    b=a[::-1]
    c=" ".join(b)
    return c
if __name__=="__main__":
    word="My Name is Prashanth Kumar Suddala I completed btech"
    print(word)
    print(reverse_words(word))
 