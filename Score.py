import sys
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

f_vec = open("vectors200_w2v.txt")
vec300 = []
for line in f_vec:
    line = line.strip("\n").strip("[").strip("]")
    line = line.split(", ")
    line = [float(num) for num in line]
    vec300.append(line)

f_w = open("unique_words_w2v.txt")
uni_words = [line.strip("\n") for line in f_w]

f_p = open("positive.txt")
p_words = [line.strip("\n") for line in f_p]

meseum_id = 0
pos_list_idx = []
for idx, word in enumerate(uni_words):
    if word == "meseum":
        meseum_id = idx
    for pos in p_words:
        if word == pos:
            pos_list_idx.append(idx)

A = np.array(vec300)
cos_matrix = cosine_similarity(A)

dic_list = []
for idx in pos_list_idx:
    dic = {}
    dic["word"] = p_words[idx]
    dic["cos"] = cos_matrix[meseum_id][idx]
    dic_list.append(dic)

dic_list = sorted(dic_list, key=lambda k: k['cos'], reverse=True)

f_out = open("score.json","w+")
f_out.write(json.dumps(dic_list, indent=4))
f_out.close()
