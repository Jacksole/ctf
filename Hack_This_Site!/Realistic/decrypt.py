#!/usr/bin/env python3.6

""" decrypt.py """
f = open('encrypted.txt')
tmp = []
arr = []
c = 0

for line in f:
    l = line.split('\n')[0]
    for i in l.split('.'):
        if i != '':
            tmp.append(int(i))
            c += 1
            if c % 3 == 0:
                arr.append(sum(tmp))
                tmp = []

# Brute force
for diff in range(max(arr)-255, min(arr)+1):
    fn = 'bruteforce-%s.txt' % diff
    bf = open(fn, 'w')
    for i in arr:
        bf.write(chr(i-diff))
    bf.close()
