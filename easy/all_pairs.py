import string
from itertools import combinations
from pprint import pprint

letters = string.ascii_letters
rooms = [letters[i] for i in range(len(letters))]
import string

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __eq__(self, other):
        return {self.first, self.second} == {other.first, other.second} and {self.first, self.second} == {other.second, other.first,}

    def __hash__(self):
        return hash(frozenset({self.first, self.second}))

    def __repr__(self):
        return f"Pair({self.first}, {self.second})"

def get_all_pairs(seq: list):
    pairs = set()
    for i in seq:
        for j in seq:
            if i != j:
                pair = Pair(i, j)
                pairs.add(pair)

    pprint(pairs)
    print(len(pairs))

get_all_pairs(rooms)


def get_all_pairs2(seq: list):
    pairs = list(combinations(string.ascii_letters, 2))
    print(len(pairs))

get_all_pairs2(rooms)
