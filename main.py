from config import *
from graphics import Window
from maze import Maze
import random
import sys


def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

    print("Maze Generator and Solver")

## Check if command line arguments exist: -C <columns> -R <rows> -S <seed> -Q (quick) -NS (no solve)

    global COLUMNS, COLUMN_WIDTH, ROWS, ROW_HEIGHT, SEED, ANIMATION_SPEED, AUTO_SOLVE
    args = sys.argv[1:]
    lArgs = [args.lower() for args in args]
    SEED = None 

    if '-c' in lArgs:
        c_index = lArgs.index('-c') + 1
        if c_index < len(args):
            try:
                COLUMNS = int(args[c_index])
            except ValueError:
                print("Columns must be an integer.")
                sys.exit(1)
    else: COLUMNS = 16

    if '-r' in lArgs:
        r_index = lArgs.index('-r') + 1
        if r_index < len(args):
            try:
                ROWS = int(args[r_index])
            except ValueError:
                print("Rows must be an integer.")
                sys.exit(1)
    else: ROWS = 10

    if '-s' in lArgs:
        s_index = lArgs.index('-s') + 1
        if s_index < len(args):
            try:
                SEED = int(args[s_index])
            except ValueError:
                print("Seed must be an integer.")
                sys.exit(1)

    if '-q' in lArgs:
        ANIMATION_SPEED = 0.0
    else:
        ANIMATION_SPEED = 0.05

    if '-ns' in lArgs:
        AUTO_SOLVE = False
    else:
        AUTO_SOLVE = True

    if '--help' in lArgs or '-h' in lArgs:
        print("Usage: python main.py [-C <columns>] [-R <rows>] [-S <seed>] [-Q] [-NS]")
        print(" -C <columns> : Set number of columns in the maze (default: 16)")
        print(" -R <rows>    : Set number of rows in the maze (default: 10)")
        print(" -S <seed>    : Set random seed for maze generation (Integer value)")
        print(" -Q           : Quick mode (no animation)")
        print(" -NS          : No auto-solve")
        sys.exit(0)

    ROW_HEIGHT = (SCREEN_HEIGHT - (2 * MARGIN)) / ROWS
    COLUMN_WIDTH = (SCREEN_WIDTH - (2 * MARGIN)) / COLUMNS

    if SEED is not None:
        print(f"Using seed: {SEED}")
    else: 
        print("Using random seed")

    maze = Maze(MARGIN, MARGIN, ROWS, COLUMNS, COLUMN_WIDTH, ROW_HEIGHT, ANIMATION_SPEED, AUTO_SOLVE, SEED, win )

    win.wait_for_close()


main()
