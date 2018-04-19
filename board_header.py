#!/usr/bin/python
class node:
    def __init__(self):
        self.data = None
        self.up = None
        self.down = None
        self.left = None
        self.right = None

class board:
    def __init__(self,board_size_x,board_size_y):
        self.cur_node = node()
        self.origin_node = self.cur_node
        self.cursor = None
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.create_board()
        self.cur_node = self.origin_node

    def create_board(self):
        for iy in range(0,self.board_size_y-1):
            self.cur_node = self.origin_node
            for iy2 in range(0,iy):
                self.cur_node = self.cur_node.down
            for ix in range(0,self.board_size_x-1):
                self.create_2x2()
                self.cur_node = self.cur_node.right    

    def create_2x2(self):
        if (self.cur_node.right == None):
            self.create_right_node()
        if (self.cur_node.down == None):
            self.create_down_node()

        self.create_down_right_node()
   
    def create_right_node(self):
        new_node = node()
        self.cur_node.right = new_node
        new_node.left = self.cur_node

    def create_down_node(self):
        new_node = node()
        self.cur_node.down = new_node
        new_node.up = self.cur_node

    def create_down_right_node(self):
        new_node = node()
        new_node.up = self.cur_node.right
        new_node.left = self.cur_node.down
       
        self.cur_node.down.right = new_node
        self.cur_node.right.down = new_node

