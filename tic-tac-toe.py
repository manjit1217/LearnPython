# import numpy as np
# import tkinter
# matrix = {'0': '', '1': '', '2': '',
#             '3': '', '4': '', '5': '',
#             '6': '', '7': '', '8': ''}
# # print("Enter the entries rowwise:")
# # x=np.array(list(matrix.values())).reshape(3,3)
# # x[1][1]='V'
# # print(x)
#
#
# print(list(matrix.values()))
# print(len(matrix.values()))
#
# window = tkinter.Tk()
#
# btn_text = tkinter.StringVar()
# x=list(matrix.values())
# print(x)
# btnlist=[]
# count=0
# total=0


def resultCheck(boardList):
    print(boardList[0:3])
    if (len(set(boardList[0:3]))==1):
        print("Winner is :"+boardList[0])
    elif(len(set(boardList[3:6]))==1):
        print("Winner is :" + boardList[3])
    elif(len(set(boardList[6:9]))==1):
        print("Winner is :" + boardList[6])
    elif(len(set(boardList[0:9:3])) == 1):
        print("Winner is :" + boardList[0])
    elif (len(set(boardList[1:9:3])) == 1):
        print("Winner is :" + boardList[1])
    elif (len(set(boardList[2:9:3])) == 1):
        print("Winner is :" + boardList[2])
        print(boardList[2:8:2])
    elif (len(set(boardList[0:12:4])) == 1):
        print("Winner is :" + boardList[0])
    elif(len(set(boardList[2:7:2]))==1):
        print("Winner is :" + boardList[2])
    else:print("Match is tie")

x=['O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'X']

resultCheck(x)
# def onClick(index):
#     onClick.counter+=1
#     global total
#
#     countnull=1
#     for i,j in matrix.items():
#         if(j==''):
#             countnull=countnull+1
#
#     if(countnull%2==0):
#         btnlist[index]['text'] = 'O'
#         matrix[str(index)] ='O'
#         print(matrix)
#     else:
#         btnlist[index]['text'] = 'X'
#         matrix[str(index)] ='X'
#     total=total+1
#     print('check')
#     if (onClick.counter == 9):
#         resultCheck(list(matrix.values()))
#
# onClick.counter=0
#
#
#
#
# for i in range(3):
#     for j in range(3):
#         button = tkinter.Button(window, pady=2, height=10, width=10, command=lambda idx = count: onClick(idx))
#         button.grid(row=i, column=j, pady=10)
#         count=count+1
#         btnlist.append(button)
# print(count)
# print(btnlist)
#
# window.mainloop()
#
# # For user input
# # for i in range(3):  # A for loop for row entries
# #     a = []
# #     for j in range(3):  # A for loop for column entries
# #         a.append(matrix.values())
# #     x.append(a)
# #
# print(list(x))