import threading
import collections

def baca_text(file):
    buka = open(file)
    baca = buka.read()
    baca_split = baca.split()
    ambil=collections.Counter(baca_split).most_common()
    for kata in ambil:
        print("%s\t: %d"%(kata[0],kata[1]))

files = [
        '1.txt',
        '2.txt',
        '3.txt',
        '4.txt',
        '5.txt',
        '6.txt',
        '7.txt',
        '8.txt',
        '9.txt'
]

for file in files:
    baca_text(file)
