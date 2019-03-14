import re
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

from gensim.models import word2vec as w2


class Word2Vec:

    def __init__(self):
        pass

    @staticmethod
    def WORD2VEC(list):
        model = w2.Word2Vec(list)
        w2v = dict(zip(model.wv.index2word, model.wv.syn0))
        return w2v
