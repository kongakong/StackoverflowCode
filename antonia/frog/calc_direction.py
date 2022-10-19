#!/usr/bin/env python3
from pprint import pprint

game_board = []

# similar to c struct
class Bug:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def move_bug(bug, x_direction, y_direction, move_step):
    global game_board     
    old_x_pos = bug.x
    old_y_pos = bug.y
    bug.x = bug.x + move_step * x_direction
    bug.y = bug.y + move_step * y_direction
    game_board[old_y_pos][old_x_pos] = "L"
    game_board[bug.y][bug.x] = "B"
    pprint(game_board)



def main():

    global game_board 
    game_board = []
    for i in range(0, 9):
        game_board.append(["~"] * 9)

    # set B at row 8, col 3
    game_board[7] = ["L"] * 9

    move_step = 1
    x_direction = 1  # 0 for no move, 1 for right, -1 for left
    y_direction = 0  # 0 for no move, 1 for down, -1 for up

    bug = Bug(y=7, x=2)
    # print(bug.x, bug.y)
    game_board[bug.y][bug.x] = "B"

    pprint(game_board)

    # let move B to right
    print("Move to right (1)")
    move_bug(bug, 1, 0, 1)

    # let move B to right
    print("Move to left (-1)")
    move_bug(bug, -1, 0, 1)
    
    print("Move up (-1)")
    move_bug(bug, 0, -1, 1)

if __name__ == "__main__":
    main()
