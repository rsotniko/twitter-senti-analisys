class Rectangle:
    user = " "
    theme = " "
    mainTxt = " "

    def med(self):
        return 10


_list = []
f = open('123')

text = f.readline()
while text:
    _r = Rectangle()
    _list.append(_r)
    print(text, end='')
    text = f.readline()

f.close()
_r = Rectangle()
print('\n' + str(_r.med()))