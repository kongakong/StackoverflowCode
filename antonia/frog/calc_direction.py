#!/usr/bin/env python3
from pprint import pprint

game_board = []

# similar to c struct
class Bug:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Tile:
    def __init__(self, is_log=False, has_bug=False):
        self.is_log = is_log
        self.has_bug = has_bug

    def __str__(self):
        if self.has_bug:
            return "B"
        return "L" if self.is_log else "~"


def print_board():
    global game_board     
    for rows in game_board:
        row_line = ",".join(str(tile) for tile in rows)
        print(row_line)
    print("\n")

def move_bug(bug, x_direction, y_direction, move_step):
    global game_board     
    old_x_pos = bug.x
    old_y_pos = bug.y
    bug.x = bug.x + move_step * x_direction
    bug.y = bug.y + move_step * y_direction
    game_board[old_y_pos][old_x_pos].has_bug = False
    game_board[bug.y][bug.x].has_bug = True 
    print_board()



def main():

    global game_board 
    game_board = []
    for y in range(0, 9):
        board_row = []
        for x in range(0, 9):
            board_row.append(Tile(is_log=True if y == 7 else False))
        game_board.append(board_row)

    print_board()

    # explain the directionality
    move_step = 1
    x_direction = 1  # 0 for no move, 1 for right, -1 for left
    y_direction = 0  # 0 for no move, 1 for down, -1 for up

    bug = Bug(y=7, x=2)
    game_board[bug.y][bug.x].has_bug = True
    print_board()

    # let move B to right
    print("Move to right (1)")
    move_bug(bug, 1, 0, 1)

    # let move B to right
    print("Move to left (-1)")
    move_bug(bug, -1, 0, 1)
    
    print("Move up (-1)")
    move_bug(bug, 0, -1, 1)

    move_bug(bug, 0, -1, 1)


if __name__ == "__main__":
    main()
