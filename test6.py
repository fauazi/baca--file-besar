from collections import Counter

def count_word(rajarimba):
        with open('rajarimba.txt') as f:
                return Counter(f.read().split())

print(count_word('rajarimba'))