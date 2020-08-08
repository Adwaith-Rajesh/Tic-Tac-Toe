# This is where the gui for the tic Tac Toe game will be made
"""
author: Adwaith Rajesh, @adwaith_rajesh
follow me on Instagram
This is a basic Tic Tac Toe Game, Hope you will enjoy it.

"""
# import all the necessary modules
from tkinter import *
from TicLogic import *
from pymsgbox import confirm
from time import sleep


class TicTacToe:

    def __init__(self):
        self.XO = XorO()
        self.master_list = []
        self.master_dict = {1: 'a', 2: 'a', 3: 'a', 4: 'a', 5: 'a', 6: 'a', 7: 'a', 8: 'a', 9: 'a'}
        self.CW = Check_Winner(self.master_dict)

        # The gui part

        self.master = Tk()
        self.master.title('Tic Tac Toe')
        self.master.geometry('295x285+500+250')
        self.master.resizable(0, 0)

        # All the buttons
        self.btn1 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(1))
        self.btn1.grid(row=0, column=0)

        self.btn2 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(2))
        self.btn2.grid(row=0, column=1)

        self.btn3 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(3))
        self.btn3.grid(row=0, column=2)

        self.btn4 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(4))
        self.btn4.grid(row=1, column=0)

        self.btn5 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(5))
        self.btn5.grid(row=1, column=1)

        self.btn6 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(6))
        self.btn6.grid(row=1, column=2)

        self.btn7 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(7))
        self.btn7.grid(row=2, column=0)

        self.btn8 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(8))
        self.btn8.grid(row=2, column=1)

        self.btn9 = Button(self.master, text='', height=5, width=10, padx=10, pady=5, command=lambda: self.button(9))
        self.btn9.grid(row=2, column=2)

        self.master.mainloop()

    def button(self, num):
        button_dict = {
            1: self.btn1,
            2: self.btn2,
            3: self.btn3,
            4: self.btn4,
            5: self.btn5,
            6: self.btn6,
            7: self.btn7,
            8: self.btn8,
            9: self.btn9
        }
        if num not in self.master_list and self.CW.winner == 0:  # Prevents a button from showing two values or once clicked,
            # cannot be clicked again

            btn = button_dict.get(num)
            value = self.XO.value
            if value == 'X':
                btn.config(bg='Light Blue')

            else:
                btn.config(bg='White')
            btn.config(text=value)

            self.master_dict[num] = value
            self.XO.change_value()  # Changes the value to X if the current value is o
            # Change the value to o if the current value is X

            self.master_list.append(num)
            self.CW.start()

            if self.CW.winner != 0:
                if self.CW.winner == 1:
                    self.master.update()
                    sleep(0.5)
                    ask = confirm(title='Tic tac Toe', text='X Won the game !, Would you like to continue ?')
                    if ask == 'OK':
                        self.Reset()

                    else:
                        self.master.quit()
                        self.master.withdraw()
                elif self.CW.winner == 2:
                    self.master.update()
                    sleep(0.5)
                    ask = confirm(title='Tic tac Toe', text='O Won the game !, Would you like to continue ?')
                    if ask == 'OK':
                        self.Reset()

                    else:
                        self.master.quit()
                        self.master.withdraw()

                else:
                    self.master.update()
                    sleep(0.5)
                    ask = confirm(title='Tic tac Toe', text='It\'s a Draw !, Would you like to continue ?')
                    if ask == 'OK':
                        self.Reset()

                    else:
                        self.master.quit()
                        self.master.withdraw()

    def Reset(self):
        button_dict = {
            1: self.btn1,
            2: self.btn2,
            3: self.btn3,
            4: self.btn4,
            5: self.btn5,
            6: self.btn6,
            7: self.btn7,
            8: self.btn8,
            9: self.btn9
        }

        for i in button_dict:
            a = button_dict.get(i)
            a.config(text='')
            a.config(bg='light grey')

        self.master_list.clear()

        for j in self.master_dict:
            self.master_dict[j] = 'a'

        self.XO.Reset()
        self.CW.Reset()


T = TicTacToe()
