#!/usr/bin/python
from simple_implementation import *

x = simple_game(10,3)
x.print_board()
while True:
    op = input()
    if (op == 'w'):
        x.move_up()
    elif (op == 's'):
        x.move_down()
    elif (op == 'a'):
        x.move_left()
    elif (op == 'd'):
        x.move_right()

    x.print_board()

