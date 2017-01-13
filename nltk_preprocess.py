#!/usr/bin/env python

import nltk
import string
import sys
from nltk.corpus import stopwords
import re

filename = sys.argv[1]
fout1 = open('%s_stemmed.txt' % filename, 'w')
stopwords = set(stopwords.words('english'))
stemmer = nltk.stem.PorterStemmer()

# stemming the dictionary
lines = [line.strip() for line in open('%s.txt' % filename)]

lines_processed = []
for idx in range(0,len(lines)):
    words = re.sub(r'[^\w]', ' ',lines[idx]).split(' ')
    words[-1] = words[-1].strip()
    words_stop_removed = [w.lower() for w in words if w.lower() not in stopwords]
    words_stemmed = [stemmer.stem(w) if '_' not in w else w for w in words_stop_removed]
    lines_processed.append(' '.join(words_stemmed))

results = []
for idx in range(0,len(lines)):
    results.append(' '.join(lines_processed[idx].split()))

fout1.write("\n".join(results))
fout1.write("\n")

#########################
