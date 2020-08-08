"""
This is the main file of the AI game..
This game is a continuation of the game Tic Tac Toe Manual

Author: Adwaith Rajesh @adwaith__rajesh

"""

# modules
from tkinter import *
from logic import *
from time import sleep
from pymsgbox import alert, INFO, confirm, OK_TEXT, CANCEL_TEXT


# create the class TicTacToe which holds all the gui part of the game
class TicTacToe:

    def __init__(self):
        self.check_list = []
        self.pos_element_list = [None] * 9
        self.check_value = 0

        self.decide = Decide(self.pos_element_list)

        self.master = Tk()
        self.master.geometry('415x440+500+250')
        self.master.resizable(0, 0)
        self.master.title('Tic Tac Toe AI @adwaith_rajesh')

        # The Gui
        self.btn1 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(0))
        self.btn1.grid(row=0, column=0)
        self.btn2 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(1))
        self.btn2.grid(row=0, column=1)
        self.btn3 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(2))
        self.btn3.grid(row=0, column=2)
        self.btn4 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(3))
        self.btn4.grid(row=1, column=0)
        self.btn5 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(4))
        self.btn5.grid(row=1, column=1)
        self.btn6 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(5))
        self.btn6.grid(row=1, column=2)
        self.btn7 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(6))
        self.btn7.grid(row=2, column=0)
        self.btn8 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(7))
        self.btn8.grid(row=2, column=1)
        self.btn9 = Button(self.master, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8
                           , command=lambda: self.OnClick(8))
        self.btn9.grid(row=2, column=2)

        self.master.mainloop()

    def OnClick(self,num):
        inside_dict = {
            0: self.btn1,
            1: self.btn2,
            2: self.btn3,
            3: self.btn4,
            4: self.btn5,
            5: self.btn6,
            6: self.btn7,
            7: self.btn8,
            8: self.btn9
        }

        if num not in self.check_list and self.check_value == 0:
            # This is the X part or the player part
            self.check_list.append(num)
            inside_dict.get(num).config(text='X', bg='light blue')
            self.pos_element_list[num] = 'X'

            # print(self.check_list, self.pos_element_list)
            # The Ai Part
            move = self.decide.Move()

            if move is not None:
                inside_dict.get(move).config(text='O', bg='blue')
                self.check_list.append(move)
                self.pos_element_list[move] = 'O'

            self.decide.IsWinner()
            val = self.decide.winner
            if val == 1:
                self.check_value = 1
                self.master.update()
                sleep(0.5)
                alert(text='X Won the Game !', title='Tic Tac Toe', icon=INFO)
                sleep(1)
                self.Quit()

            elif val == 2:
                self.check_value = 2
                self.master.update()
                sleep(0.5)
                alert(text='O Won the Game !', title='Tic Tac Toe', icon=INFO)
                sleep(1)
                self.Quit()

            elif val == 3:
                self.check_value = 3
                self.master.update()
                sleep(0.5)
                alert(text='The Game is Draw !', title='Tic Tac Toe', icon=INFO)
                sleep(1)
                self.Quit()

    def Quit(self):
        self.master.quit()
        self.master.destroy()
        sleep(0.5)

        val = confirm(text='Would you like to continue ?', title='Tic Tac Toe', buttons=(OK_TEXT, CANCEL_TEXT))
        if val == 'OK':
            start()
        else:
            return


def start():
    TTT = TicTacToe()


if __name__ == "__main__":
    start()
