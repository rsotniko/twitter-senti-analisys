'''
File 123 include test strings for parsing
'''

class Data:
    user = " "
    theme = " "
    mainTxt = " "

    def Parse(self, stream):
        _str = Data()
        stream = stream.replace(" ", "", len(stream))
        try:
            _str.user = stream.split(';', 3)[0]
            _str.theme = stream.split(';', 3)[1]
            _str.mainTxt = stream.split(';', 3)[2]
        except Exception:
            _str.user = "user ignored"
            _str.theme = "user ignored"
            _str.mainTxt = "user ignored"

        return _str

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


# This code just represent the work of class above
_list = Data.ParseFullFile('123')
i = 0
while i < len(_list):
    a = i + 1
    print("User number " + a.__str__() + "\n_____________________________\n")
    print("User name: " + _list[i].user)
    print("Theme: " +_list[i].theme)
    print("Text: " +_list[i].mainTxt)
    print("_____________________________\n")
    i += 1
