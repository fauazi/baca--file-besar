import collections


with open('file1.txt') as f:
    op = f.readlines()

count = 0
for line in op:
    count += 1
    if count == 1000000:
        break
    be = line.split()
    print(be)
    
