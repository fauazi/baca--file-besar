from collections import Counter
with open('rajarimba.txt') as f:
    baca = f.readlines

txt = Counter(baca)
dict = {}

for letter in txt:
    dict[letter] = txt[letter]

print(baca)