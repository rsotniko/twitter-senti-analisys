"""
Файл 123 содержит данные для проверки парсера, самое простые исключения обработаны
"""


class Data:
    user = " "
    theme = " "
    mainTxt = " "

    def Parse(self, stream):
        _str = Data()
        stream = stream.replace(" ", "", len(stream))
        # Если хоть в одном поле нет информации о поле или неверный вормат данных запишем в строку, что данные для
        # пользователя  данные некорректны, если хоть 1 строка некорректна пользователь получит оповещение об этом
        try:
            _str.user = stream.split(';', 3)[0]
            _str.theme = stream.split(';', 3)[1]
            _str.mainTxt = stream.split(';', 3)[2]
        except Exception:
            print("_____________________________\n\nATTENTION: File has ivalid strings\n_____________________________\n")
            _str.user = "user ignored"
            _str.theme = "user ignored"
            _str.mainTxt = "user ignored"

        return _str

    @staticmethod
    def ParseFullFile(_fileName):
        _list = []
        try:
            f = open(_fileName)
        except Exception:  # Надо сделать менее общее исключение
            print("Invalid filename or file is corrupted")
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
i = 0
while i < len(_list):
    a = i + 1
    print("Информация о пользователь №" + a.__str__() + "\n_____________________________")
    print("User Name: " + _list[i].user)
    print("Theme: " +_list[i].theme)
    print("Text: " +_list[i].mainTxt)
    print("_____________________________\n")
    i += 1
