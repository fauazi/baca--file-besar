import collections

f = open('rajarimba.txt', 'r')
baca = f.read()
buka_list = baca.split()
ambil=collections.Counter(buka_list).most_common()

for kata in ambil:
    print("%s\t: %d"%(kata[0],kata[1]))

print(buka_list)

