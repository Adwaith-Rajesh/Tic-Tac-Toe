"""
This is the logic part of the game..

author: Adwaith Rajesh @adwaith__rajesh

It contains all the movements of the game
"""


# Class to decide where to place all the O
class Decide:
    def __init__(self, place_list):
        self.places = place_list
        self.check_list = []
        self.winner = 0  # 1 if X won 2 if O won

    # The number it return coincides with the dict in the OnClick method int the main module
    def Move(self):
        # To get the pos of x
        for x, y in enumerate(self.places):
            if y == 'X' and x not in self.check_list:
                self.check_list.append(x)

        if self.places[4] is None:
            self.check_list.append(4)
            return 4

        else:
            if self.places[6] is None and 4 not in self.check_list:
                self.check_list.append(6)
                return 6
            else:
                for i in range(8):
                    if i == 0:
                        if self.places[0] == 'X' and self.places[1] == 'X' and 2 not in self.check_list and self.places[2] is None:
                            self.check_list.append(2)
                            return 2  # the pos to place 'O'

                        if self.places[0] == 'X' and self.places[2] == 'X' and 1 not in self.check_list and self.places[1] is None:
                            self.check_list.append(1)
                            return 1

                        if self.places[0] == 'X' and self.places[3] == 'X' and 6 not in self.check_list and self.places[6] is None:
                            self.check_list.append(6)
                            return 6

                        if self.places[0] == 'X' and self.places[6] == 'X' and 3 not in self.check_list and self.places[3] is None:
                            self.check_list.append(3)
                            return 3

                        if self.places[0] == 'X' and self.places[8] == 'X' and 4 not in self.check_list and self.places[4] is None:
                            self.check_list.append(4)
                            return 4

                    if i == 1:
                        if self.places[1] == 'X' and self.places[2] == 'X' and 0 not in self.check_list and self.places[0] is None:
                            self.check_list.append(0)
                            return 0

                        if self.places[1] == 'X' and self.places[4] == 'X' and 7 not in self.check_list and self.places[7] is None:
                            self.check_list.append(7)
                            return 7

                        if self.places[1] == 'X' and self.places[7] == 'X' and 4 not in self.check_list and self.places[4] is None:
                            self.check_list.append(4)
                            return 4

                    if i == 2:
                        if self.places[2] == 'X' and self.places[5] == 'X' and 8 not in self.check_list and self.places[8] is None:
                            self.check_list.append(8)
                            return 8

                        if self.places[2] == 'X' and self.places[4] == 'X' and 6 not in self.check_list and self.places[6] is None:
                            self.check_list.append(6)
                            return 6

                        if self.places[2] == 'X' and self.places[6] == 'X' and 4 not in self.check_list and self.places[4] is None:
                            self.check_list.append(4)
                            return 4

                        if self.places[2] == 'X' and self.places[8] == 'X' and 5 not in self.check_list and self.places[5] is None:
                            self.check_list.append(5)
                            return 5

                    if i == 3:
                        if self.places[3] == 'X' and self.places[6] == 'X' and 0 not in self.check_list and self.places[0] is None:
                            self.check_list.append(0)
                            return 0

                        if self.places[3] == 'X' and self.places[4] == 'X' and 5 not in self.check_list and self.places[5] is None:
                            self.check_list.append(5)
                            return 5

                        if self.places[3] == 'X' and self.places[5] == 'X' and 4 not in self.check_list and self.places[4] is None:
                            self.check_list.append(4)
                            return 4

                    if i == 4:
                        if self.places[4] == 'X' and self.places[5] == 'X' and 3 not in self.check_list and self.places[3] is None:
                            self.check_list.append(3)
                            return 3

                        if self.places[4] == 'X' and self.places[7] == 'X'and 1 not in self.check_list and self.places[1] is None:
                            self.check_list.append(1)
                            return 1

                        if self.places[4] == 'X' and self.places[6] == 'X' and 2 not in self.check_list and self.places[2] is None:
                            self.check_list.append(2)
                            return 2

                        if self.places[4] == 'X' and self.places[8] == 'X' and 0 not in self.check_list and self.places[0] is None:
                            self.check_list.append(0)
                            return 0

                    if i == 5:
                        if self.places[5] == 'X' and self.places[8] == 'X' and 2 not in self.check_list and self.places[2] is None:
                            self.check_list.append(2)
                            return 2

                    if i == 6:
                        if self.places[6] == 'X' and self.places[7] == 'X' and 8 not in self.check_list and self.places[8] is None:
                            self.check_list.append(8)
                            return 8

                        if self.places[6] == 'X' and self.places[8] == 'X' and 7 not in self.check_list and self.places[7] is None:
                            self.check_list.append(7)
                            return 7

                    if i == 7:
                        if self.places[7] == 'X' and self.places[8] == 'X' and 6 not in self.check_list and self.places[6] is None:
                            self.check_list.append(6)
                            return 6

                    if i == 8:
                        pass
                else:
                    for j in self.places:
                        if j is None:
                            val = int(self.places.index(j))
                            return val

    def IsWinner(self):
        list1 = self.places
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
        if None not in self.places:
            self.winner = 3
