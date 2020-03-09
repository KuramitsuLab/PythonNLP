# -*- coding: utf-8 -*-

f = open('../data/kusamakura.txt','r')

line = 0
word = 0

for i in f:
    line += 1
    word += len(i)

print(line)
print(word)


f.close()