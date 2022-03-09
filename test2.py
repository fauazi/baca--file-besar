kata = 'rimba'
count = 0
with open('rajarimba.txt') as f:
    for line in f:
        angka = count + line.count(kata) 
        angka =+ 1


print(angka)