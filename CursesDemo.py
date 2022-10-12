#CursesDemo

import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr('hello world!')
    stdscr.getch()

wrapper(main)