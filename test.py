import tkinter

root = tkinter.Tk()
frm = tkinter.Frame(root)
frm.grid()
tkinter.Label(frm, text="Hello World!").grid(column=0, row=0)
tkinter.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
root.mainloop()


# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# import numpy as np
# import pandas as pd

# class ChessBoard:
#     #defining the varialble for the requirements in the board
#     board, white, blue, red, blue_pos, red_pos = np.zeros((8,8,3)), (1,1,1), (0,1,1), (1,.2,0), [], []
# #     x = [a,b,c,d,e,f,g,h]
# #     y = [1,2,3,4,5,6,7,8]
#     def __init__(self):
#         #initiating the ChessBoard with the creation of it's board
#         ChessBoard.board = np.zeros((8,8,3))
#         for i in range(8):
#             for j in range(8):
#                 if (i%2 == j%2):
#                     ChessBoard.board[i][j] = ChessBoard.white
#     def add_red(self, pos1, pos2):
#         ChessBoard.board[pos1][pos2] = ChessBoard.red
#         ChessBoard.red_pos = [pos1, pos2]
#     def add_blue(self, pos1, pos2):
#         ChessBoard.board[pos1][pos2] = ChessBoard.blue
#         ChessBoard.blue_pos = [pos1, pos2]
#     # adding the render function 
    
#     def render(self):
#         plt.imshow(ChessBoard.board)
        
#     def is_under_attack(self):
#     # if x-axis match
#         if ChessBoard.blue_pos[0] == ChessBoard.red_pos[0]:
#             return True
#         # if y-axis match
#         if ChessBoard.blue_pos[1] == ChessBoard.red_pos[1]:
#             return True
#         # if diagonal-axis match
#         if abs(ChessBoard.blue_pos[1] - ChessBoard.red_pos[1]) == abs(ChessBoard.blue_pos[0] - ChessBoard.red_pos[0]):
#             return True
#         # else return false
#         return False


# board5 = ChessBoard()
# board5.add_red(0,3)
# board5.add_blue(7,3)
# board5.render()

# board5.is_under_attack()