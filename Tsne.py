import sys
import numpy as np
import json
import re
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

class Tsne:

    def __init__(self):
        self.src = sys.argv[1]
        self.array = []
        self.words = []
        self.dim2 = []

    def get_data(self):
        f_w = open("unique_words_w2v.txt")
        self.words = [line.strip("\n") for line in f_w]
        f = open(self.src)
        for line in f:
            line = line.strip("\n").strip("[").strip("]")
            vector = line.split(", ")
            #self.words.append(vector[0])
            #vector = vector[1:-1]
            vector = [float(num) for num in vector]
            self.array.append(vector)

    def dim_deduction(self):
        #pca = PCA(n_components=30)
        #print "pca start.."
        #pca.fit(self.array)
        model = TSNE(n_components=2, random_state=0)
        print "tsne start.."
        self.array = model.fit_transform(self.array)

        total = []
        for i in xrange(len(self.words)):
            line = {}
            line["index"] = i+1
            line["word"] = self.words[i]
            line["vector2"] = list(self.array[i])
            print line
            total.append(line)

        self.dim2 = total

    def render(self):
        #filename = sys.argv[1].split("/")
        #num = re.search("[0-9]+", filename[5])
        #f = open("../data/line-data/vectors/2dim/restaurant_%s_vector2.json"%num.group(0), "w+")
        f = open("vector2.json","w+")
        json.dump(self.dim2, f, indent = 4)
        f.close()

if __name__ == '__main__':
    tsne = Tsne()
    tsne.get_data()
    tsne.dim_deduction()
    tsne.render()
