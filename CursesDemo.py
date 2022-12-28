#CursesDemo

import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,1, 'hello world!', curses.A_STANDOUT)
    stdscr.addstr(0,2, 'goodby world!')
    stdscr.getch()

wrapper(main)