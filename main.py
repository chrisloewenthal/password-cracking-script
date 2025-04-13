import itertools
import random
import string


dictionary = []

with open("clean_words.txt") as f:
    dictionary = [line.strip() for line in f]

