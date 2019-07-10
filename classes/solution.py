class stringMethod(object):
    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input('Enter your name \n >')

    def string_upper(self):
        print(self.s.upper())


x = stringMethod()
x.get_string()
x.string_upper()

print(x)
