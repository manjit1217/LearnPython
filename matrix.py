#tik-toc toy game good one

import numpy as np
import tkinter
from tkinter import messagebox

from pip._vendor.html5lib.filters import optionaltags

matrix = {'0': '', '1': '', '2': '',
          '3': '', '4': '', '5': '',
          '6': '', '7': '', '8': ''}

window = tkinter.Tk()
btnlist = []
count = 0
total = 0
def result_check(board_list):
    if len(set(board_list[0:3])) == 1:
        return board_list[0]
    elif len(set(board_list[3:6])) == 1:
        return board_list[3]
    elif len(set(board_list[6:9])) == 1:
        return board_list[6]
    elif len(set(board_list[0:9:3])) == 1:
        return board_list[0]
    elif len(set(board_list[1:9:3])) == 1:
        return board_list[1]
    elif len(set(board_list[2:9:3])) == 1:
        return board_list[2]
    elif len(set(board_list[0:12:4])) == 1:
        return board_list[0]
    elif len(set(board_list[2:7:2])) == 1:
        return board_list[2]
    else:
        return 'lost'


def onClick(index):
    onClick.counter += 1
    count_null = 1
    for i, j in matrix.items():
        if j == '':
            count_null = count_null + 1
    if count_null % 2 == 0:
        btnlist[index]['text'] = 'O'
        matrix[str(index)] = 'O'
    else:
        btnlist[index]['text'] = 'X'
        matrix[str(index)] = 'X'
    print(btnlist)
    if onClick.counter == 9:
        # print(list(matrix.values()))
        result = result_check(list(matrix.values()))
        messagebox.showinfo('Result', 'winner' + result)
        # if res is True:
        #     button_create()
        # print(res)


onClick.counter = 0


def button_create():
    global count
    for i in range(3):
        for j in range(3):
            button = tkinter.Button(window, pady=2, height=10, width=10, command=lambda idx=count: onClick(idx))
            button.grid(row=i, column=j, pady=10)
            count = count + 1
            btnlist.append(button)

button_create()
window.mainloop()
