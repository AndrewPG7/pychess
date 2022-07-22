import re


class Translator:

    def __init__(self):
        self.ent = None
        self.orig = None
        self.new = None

    def valid(self):
        if re.search("[a-h][1-8] [a-h][1-8]", self.ent):
            return True
        else:
            return False

    def translate(self, ent):
        self.ent = ent
        if self.valid():

            self.orig = self.convert(self.ent[0:2])
            self.new = self.convert(self.ent[3:5])
            return True
        else:
            return False
            print('Input invalid')

    def convert(self, split):
        a = ord(split[0]) - 97
        aux = split[1]
        if aux == '1':
            b = 7
        elif aux == '2':
            b = 6
        elif aux == '3':
            b = 5
        elif aux == '4':
            b = 4
        elif aux == '5':
            b = 3
        elif aux == '6':
            b = 2
        elif aux == '7':
            b = 1
        elif aux == '8':
            b = 0
        return [b, a]
