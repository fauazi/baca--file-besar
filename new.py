import time


start = time.time()

count = 0

with open('iman.txt') as file:
    baca = file.readlines()
    
    for line in baca:
        count = count + 1

end = time.time()

#print(line)
print('terbaca dalam waktu: ', (end - start))
print('berapa baris yang ada di text: ', count)