import itertools
import random
import string


dictionary = []
special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

with open("clean_words.txt") as f:
    dictionary = [line.strip() for line in f]

#print(special_characters)
#from the spec:
#Type 1 Passphrase
#Only - characters is usued as the seperator
#All letters in all words are lowercase
def generate_type1():
    for w1, w2 in itertools.product(dictionary, repeat=2):
        yield f"{w1}-{w2}-liber8"

def generate_type2():
    for w1, w2 in itertools.product(dictionary, repeat=2):
        for sep in special_characters:
            yield f"{w1}{sep}{w2}{sep}liber8"

def generate_type3():
    
