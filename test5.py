from test6 import count_word


with open('file1.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    #print(f'{count} = {pi}')
    de = count_word('file1')

print(de)