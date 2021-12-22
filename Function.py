import random


class function(object):

    def __init__(self, length):
        """

           :param self:
            :param length:
        """
        self.length = length
        random.seed()
        self.vect = list()
        for i in range(length):
            a = random.randint(-2021, 2021)
            self.vect.append(a % 2)
        self.post_vect = str()
        self.post_vect += str(int(self.T0()))
        self.post_vect += str(int(self.T1()))
        self.post_vect += str(int(self.S()))
        self.post_vect += str(int(self.M()))
        self.post_vect += str(int(self.L()))

    # print(self.vect, '\n', self.T0(), '\n', self.T1(), '\n', self.S(), '\n', self.M(), '\n', self.L(), '\n', self.post_vect)

    def T0(self):
        if self.vect[0] == 0:
            return True
        else:
            return False

    def T1(self):
        if self.vect[self.length - 1] == 1:
            return True
        else:
            return False

    def S(self):
        for i in range(int(self.length / 2)):
            if self.vect[i] == self.vect[self.length - i - 1]:
                return False
        return True

    def L(self):
        n = {0, 1, 3, 7, 15, 31}
        for i in range(self.length):
            if self.vect[i] == 1 and i not in (n):
                return False
        return True

    def M(self):
        tmp = self.vect
        if MCheck(tmp):
            return True
        temp1 = list()
        temp2 = list()
        for i in range(4):
            temp1.append(self.vect[i])
            temp2.append(self.vect[self.length - i - 1])
        temp2.reverse()
        if MCheck(temp1) and MCheck(temp2):
            return True
        temp11 = list()
        temp12 = list()
        temp21 = list()
        temp22 = list()
        for i in range(2):
            temp11.append(self.vect[i])
            temp12.append(self.vect[int(self.length / 2) - i - 1])
            temp21.append(self.vect[int(self.length / 2) + i - 1])
            temp22.append(self.vect[self.length - i - 1])
        temp12.reverse()
        temp22.reverse()
        if MCheck(temp11) and MCheck(temp12) and MCheck(temp21) and MCheck(temp22):
            return True
        return False


def MCheck(vec):
    Alpha = list()
    Beta = list()
    for i in range(int(len(vec) / 2)):
        Alpha.append(vec[i])
        Beta.append(vec[int(len(vec) / 2) + i])
    # print(Alpha, ' ', Beta)
    if str(Alpha) >= str(Beta):
        return True
    else:
        return False