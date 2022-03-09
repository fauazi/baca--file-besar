import collections
string='PHP PYTHON JAVA PYTHON'
li=string.split(' ')
ambil=collections.Counter(li).most_common()
print(li)

for kata in ambil:
    print("%s\t: %d"%(kata[0],kata[1]))