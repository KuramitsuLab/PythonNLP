# -*- coding: utf-8 -*-

import MeCab
import sys
import re
import collections
import csv
from collections import Counter

mecab = MeCab.Tagger ('/usr/local/lib/mecab/dic/mecab-ipadic-neologd')

f = open('../data/kusamakura.txt','r')
data = f.read() 
f.close()

parse = mecab.parse(data)
lines = parse.split('\n')
items = (re.split('[\t,]', line) for line in lines)


# 名詞をリストに格納
words = [item[0]
         for item in items
         if (item[0] not in ('EOS', '', 't', 'ー') and
             item[1] == '名詞')]


# 頻度順に出力
counter = Counter(words)
for word, count in counter.most_common():
    with open('result.csv', 'a', encoding="utf_8_sig") as c:
        writer = csv.writer(c)
        writer.writerow('{0} , {1}'.format(word, count))
