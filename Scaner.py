"""
Файл 123 содержит данные для проверки парсера
"""


class Data:
    user = " "
    theme = " "
    mainTxt = " "

    def Parse(self, stream):
        _str = Data()
        stream = stream.replace(" ", "", stream.__sizeof__())
        _str.user = stream.split(';', 3)[0]
        _str.theme = stream.split(';', 3)[1]
        _str.mainTxt = stream.split(';', 3)[2]
        return _str

    @staticmethod
    def ParseFullFile(_fileName):
        _list = []
        f = open(_fileName)
        text = f.readline()
        while text:
            _r = Data()
            _r = _r.Parse(text)
            _list.append(_r)
            text = f.readline()
        f.close()
        return _list


# Для проверки работоспособности
_list = Data.ParseFullFile('123')
print(_list[1].user)
print(_list[1].mainTxt)
print(_list[2].user)
print(_list[2].mainTxt)
