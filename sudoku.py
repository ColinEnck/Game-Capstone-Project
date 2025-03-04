import curses
from curses import wrapper
import random

# given a 2D board (9x9) of ints between 0-9, print it to screen
def print_board(stdscr, board: list):
    letters = "ABCDEFGHI"
    width = 19 
    
    # top line of letters
    stdscr.addstr("  ")
    for i in range(9):
        stdscr.addstr(" " + letters[i])
    stdscr.addstr("\n")

    # top line
    stdscr.addstr("  ")
    stdscr.addch(curses.ACS_ULCORNER)
    for i in range(width - 2):
        if i % 2 == 1:
            stdscr.addch(curses.ACS_TTEE)
        else:
            stdscr.addch(curses.ACS_HLINE)
    stdscr.addch(curses.ACS_URCORNER)
    stdscr.addstr("\n")

    # the board
    for y in range(len(board)):
        # for each line, go here:
        # numbers before line
        stdscr.addstr(str(y + 1) + " ")
        # vertical line at start of line
        stdscr.addch(curses.ACS_VLINE)
        for x in range(len(board[y])):
            # for each column in each row, go here:
            # each number
            num = board[y][x]
            # if the square is empty (noted by a -1)
            if num == -1:
                stdscr.addstr(" ")
            else:
                stdscr.addstr(str(board[y][x]))
            # vertical line at left-end of square
            stdscr.addch(curses.ACS_VLINE)
        stdscr.addstr("\n")

        # bottom line for each line, but not if it is the last row
        if not y == len(board) - 1:
            stdscr.addstr("  ")
            for i in range(width):
                if i == 0:
                    stdscr.addch(curses.ACS_LTEE)
                elif i == width - 1:
                    stdscr.addch(curses.ACS_RTEE)
                # placement is important in this if-else
                # vvv only runs if it's not at the start or end of the line vvv
                elif i % 2 == 0:
                    stdscr.addch(curses.ACS_PLUS)
                else:
                    stdscr.addch(curses.ACS_HLINE)
            stdscr.addstr("\n")

    # bottom line
    stdscr.addstr("  ")
    stdscr.addch(curses.ACS_LLCORNER)
    for i in range(width - 2):
        if i % 2 == 1:
            stdscr.addch(curses.ACS_BTEE)
        else:
            stdscr.addch(curses.ACS_HLINE)
    stdscr.addch(curses.ACS_LRCORNER)
    stdscr.addstr("\n")

def main(stdscr):
    random.seed()
    # Clear screen
    stdscr.clear()
    board = []
    for y in range(9):
        line = []
        for x in range(9):
            line.append(random.randint(0, 9))
        board.append(line)
    print_board(stdscr, board)
    stdscr.getkey()

wrapper(main)