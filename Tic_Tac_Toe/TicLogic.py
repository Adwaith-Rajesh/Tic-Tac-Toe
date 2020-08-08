# This module will only contain the logic of the game>
class XorO:
    def __init__(self):
        self.value = 'X'

    def change_value(self):
        if self.value == 'X':
            # print('Inside x')
            self.value = 'O'

        elif self.value == 'O':
            # print('inside o')
            self.value = 'X'

    def Reset(self):
        self.value = 'X'


class Check_Winner:

    def __init__(self, value_dict):
        self.value_dict = value_dict
        self.master_class_list = []
        self.winner = 0  # if 1 X wins 2 Y wins 3 Draw

    def start(self):
        self.master_class_list.clear()
        self.fill()

    def fill(self):
        for x in self.value_dict.values():
            self.master_class_list.append(x)
        self.check()

    def check(self):
        list1 = self.master_class_list
        for i in ['X', 'O']:
            if ((list1[0] == i and list1[1] == i and list1[2] == i) or
                    (list1[3] == i and list1[4] == i and list1[5] == i) or
                    (list1[6] == i and list1[7] == i and list1[8] == i) or
                    (list1[0] == i and list1[3] == i and list1[6] == i) or
                    (list1[1] == i and list1[4] == i and list1[7] == i) or
                    (list1[2] == i and list1[5] == i and list1[8] == i) or
                    (list1[0] == i and list1[4] == i and list1[8] == i) or
                    (list1[2] == i and list1[4] == i and list1[6] == i)):

                if i == 'X':
                    self.winner = 1
                else:
                    self.winner = 2
                break
        else:
            self.draw()

    def draw(self):
        if 'a' not in self.master_class_list:
            self.winner = 3

    def Reset(self):
        self.master_class_list.clear()
        self.winner = 0

