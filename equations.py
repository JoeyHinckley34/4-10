from itertools import zip_longest

class equation:
    def __init__(self,strR):
        self.strRep = strR
        try:
            self.evaluation = eval(self.strRep)
        except ZeroDivisionError:
            self.evaluation = 'NaN'

    def __str__(self):
        return self.strRep + " = " + str(self.evaluation)


def test():

    a = equation('1+2+3+4')

    print(a)


#test()