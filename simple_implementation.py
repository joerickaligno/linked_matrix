#!/usr/bin/python
from board_header import *

class simple_game:
    def __init__(self,board_size_x,board_size_y):
        self.game_board = board(board_size_x,board_size_y)
        self.game_board.origin_node.data = True
        self.game_board.cur_node = self.game_board.origin_node
        self.game_board.cursor = None

    def move_up(self):
        if (self.game_board.cur_node.up != None):
            self.game_board.cur_node.data = None
            self.game_board.cur_node = self.game_board.cur_node.up 
            self.game_board.cur_node.data = True
        else:
            print("Invalid")

    def move_down(self):
        if (self.game_board.cur_node.down != None):
            self.game_board.cur_node.data = None
            self.game_board.cur_node = self.game_board.cur_node.down 
            self.game_board.cur_node.data = True
        else:
            print("Invalid")

    def move_left(self):
        if (self.game_board.cur_node.left != None):
            self.game_board.cur_node.data = None
            self.game_board.cur_node = self.game_board.cur_node.left
            self.game_board.cur_node.data = True
        else:
            print("Invalid")

    def move_right(self):
        if (self.game_board.cur_node.right != None):
            self.game_board.cur_node.data = None
            self.game_board.cur_node = self.game_board.cur_node.right
            self.game_board.cur_node.data = True
        else:
            print("Invalid")

    def print_board(self):
        for iy1 in range(0,self.game_board.board_size_y):
            self.game_board.cursor = self.game_board.origin_node
            for iy2 in range(0,iy1):
                self.game_board.cursor = self.game_board.cursor.down
            while(self.game_board.cursor != None):
                if (self.game_board.cursor.data == True):
                    print("1",end="")
                else:
                    print("0",end="")
                self.game_board.cursor = self.game_board.cursor.right

            print("")

