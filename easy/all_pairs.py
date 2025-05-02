import string
from pprint import pprint

letters = string.ascii_letters
rooms = [letters[i] for i in range(len(letters))]

def get_all_pairs(seq: list):
    is_hash = dict()
    letters = set(seq)

    for l in seq:
        is_hash[l] = letters


    pprint(is_hash)

get_all_pairs(rooms)
