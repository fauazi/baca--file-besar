with open('file1.txt', 'a') as f:
    a = input("masukan teks= ")
    b = int(input("masukan berapa banyak yang ingin dictak -> " ))
    for i in range(0,b):
        f.write(f'\n{a}')

f.close

print('=' * 30)
print("teks sudah ditambahkan")
print('=' * 30)