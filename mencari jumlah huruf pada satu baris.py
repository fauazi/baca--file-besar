with open('rajarimba.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'baris {count} :{line}=jumlah hurufnya adalah {len(line)} ')
    #bisa juga ngga count nya gak usah di tulis
