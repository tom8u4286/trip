#import itertools
import sys, os
#import uuid
import gensim

#import json

class Word2Vec:

    def __init__(self):
        """ initalize paths """
        self.src = sys.argv[1]
        self.dst_uw = "unique_words_w2v.txt"
        self.dst_v200 = "vectors200_w2v.txt"

        self.verbose = 1

    def get_source(self):
        """ get every review in backend_reviews """

        #src_files = []
        source = []
        print "Loading data from:", self.src

        cnt = 0
        length = len(os.listdir(self.src))
        for f in os.listdir(self.src):

            cnt += 1
            file_path = os.path.join(self.src, f)
            if os.path.isfile(file_path):
                #print "Found:", file_path
                with open(file_path) as f:
                   source.append(f.read())

            if self.verbose:
                sys.stdout.write("\rStatus: %s / %s"%(cnt, length))
                sys.stdout.flush()

        #print source
        return source

    def get_sentences(self):
        """ get a list of lists of words | E.g. sentences = [["sentence","one"], ["sentence","two"]] """
        source = self.get_source()

        sentences = []
        for sentence in source:
            sentences.append(sentence.split())

        #print sentences
        return sentences

    def run_word2vec(self):
        """ run word to vector """
        sentences = self.get_sentences()

        print '\n' + '-'*80
        print "Running Word2Vec"
        model = gensim.models.Word2Vec(sentences, min_count=3, size=300, window = 10, workers=4)
        model.train(sentences)
        model.intersect_word2vec_format("GoogleNews-vectors-negative300.bin",binary=True)
        unique_words = list(model.vocab.keys())

        vectors200 = []
        for word in unique_words:
            vectors200.append(model[word].tolist())

        #print unique_words, vectors200
        return unique_words, vectors200

    def create_folder(self):
        """ create folder (1) coreProcess_input """
        dir1 = os.path.dirname("data/coreProcess_word2vec/")
        if not os.path.exists(dir1):   # if the directory does not exist
            os.makedirs(dir1)          # create the directory

    def render(self):
        """ render into two files """
        unique_words, vectors200 = self.run_word2vec()
        #self.create_folder()

        print "-"*80
        print "Writing data to", self.dst_uw
        with open(self.dst_uw, 'w+') as f1:
            for word in unique_words:
                f1.write( word + "\n")

        print "Writing data to", self.dst_v200
        with open(self.dst_v200, 'w+') as f2:
            for vector in vectors200:
                f2.write(str(vector) + '\n')

if __name__ == '__main__':
    word2vec = Word2Vec()
    word2vec.render()

