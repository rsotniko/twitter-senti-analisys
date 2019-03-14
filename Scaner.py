'''
File 123 include test strings for parsing
Before running install pymorphy2 in console using pip
Valid string format: UserName;theme;sampleText;
'''

import word2vec
import re
import pymorphy2
import numpy as np

morph = pymorphy2.MorphAnalyzer()


class Data:
    user = " "
    theme = " "
    mainTxt = []  # contains list of words, for analisys

    # Parse 1 element
    def Parse(self, stream):
        _str = Data()
        try:
            _str.user = stream.split(';', 3)[0]
            _str.theme = stream.split(';', 3)[1]
            _str.mainTxt = Data.review_to_wordlist(stream.split(';', 3)[2])
        except Exception:
            _str.user = "Invalid data"
            _str.theme = "Invalid data"
            _str.mainTxt = "Invalid data"

        return _str

    # Parse all elements using method Parse
    @staticmethod
    def ParseFullFile(_fileName):
        _list = []
        try:
            f = open(_fileName)
        except Exception:
            print("Invalid filename or file is corrupted")
        text = f.readline()
        while text:
            _r = Data()
            _r = _r.Parse(text)
            _list.append(_r)
            text = f.readline()
        f.close()
        return _list

    # Return a list of words, in correct form
    @staticmethod
    def review_to_wordlist(review):
        # Delete all simbols, exept uppercase and lowercase letters
        review_text = re.sub("[^a-zA-Z]", " ", review)
        # Converting uppercase to lowercase letters
        words = review_text.lower().split()
        # Converting to normal
        words = [morph.parse(w)[0].normal_form for w in words]
        return (words)


'''
ATTENTION CODE BELOW IS FOR DEMONSTRATION ONLY,
SHOULD BE DELETED AFTER
'''


class List:
    @staticmethod
    def list_print(_list):
        j = 0;
        if _list == "Invalid data":
            print ("Invalid data")
        else:
            for i in _list:
                print("Element number " + j.__str__() + " " + i.__str__() + "\n")
                j += 1;


# This code just represent the work of class above
_list = Data.ParseFullFile('123')
Data = pd.read_csv('123')
#i = 0
# while i < len(_list):
#     a = i + 1
#     print("User number " + a.__str__() + "\n_____________________________\n")
#     print("User name: " + _list[i].user)
#     print("Theme: " + _list[i].theme)
#     List.list_print(_list[i].mainTxt)
#     print("_____________________________\n")
#     i += 1
Data['list_w'] = Data['text'].apply(lambda x: x.split(','))
Data = word2vec.Word2Vec.WORD2VEC(Data['list_w'])
# for i in Data:
#     print(i)