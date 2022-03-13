import threading
import collections

def baca_text(file):
    buka = open(file)
    baca = buka.read()
    baca_split = baca.split()
    ambil=collections.Counter(baca_split).most_common()
    for kata in ambil:
        tambah = open('iman.txt', 'a')
        tambah.write("%s\t: %d\n"%(kata[0],kata[1]))

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

threads = []
for file in files:
	t = threading.Thread(target=baca_text, args=(file,))
	threads.append(t)

for t in threads:
	t.start()


for t in threads:
	t.join()