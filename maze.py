from config import *
from cell import Cell
import random
import time
import sys

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        animation_speed,
        solve,
        seed = None,
        win = None
    ):
        self.__cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__animation_speed = animation_speed
        self.__solve = solve
        self.__seed = seed
        self.__win = win
        self.solve_visited_cells = 0
        self.path_length = 0

        if self.__seed is not None:
            random.seed(self.__seed)

        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0,0)
        self.__reset_cells_visited()
        if self.__solve:
            self.__solve_r(0,0)

    def __create_cells(self):
        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__win))
            self.__cells.append(col_cells)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.__win is None:
            return
        try:
            x1 = self.__x1 + i * self.__cell_size_x
            y1 = self.__y1 + j * self.__cell_size_y
            x2 = x1 + self.__cell_size_x
            y2 = y1 + self.__cell_size_y
            self.__cells[i][j].draw(x1, y1, x2, y2)
            self.__animate()
        except KeyboardInterrupt:
            print("\nMaze Construction interrupted.")
            sys.exit(0)

    def __animate(self):
        if self.__win is None:
            return
        try:
            self.__win.redraw()
            time.sleep(self.__animation_speed)
        except KeyboardInterrupt:
            print("\nMaze Animation interrupted.")
            sys.exit(0)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.__cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.__num_cols - 1 and not self.__cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.__cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.__num_rows - 1 and not self.__cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self.__draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.__break_walls_r(next_index[0], next_index[1])

    def __reset_cells_visited(self):
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__cells[i][j].visited = False

    def __solve_r(self, i, j):
        self.__cells[i][j].visited = True
        self.solve_visited_cells += 1

        # if we have reached the exit
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            self.path_length += 1
            return True

        # try to move in each direction
        # left
        if (
            i > 0
            and not self.__cells[i][j].has_left_wall
            and not self.__cells[i - 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i - 1][j])
            self.__animate()
            if self.__solve_r(i - 1, j):
                self.path_length += 1
                return True
            self.__cells[i][j].draw_move(self.__cells[i - 1][j], undo=True)
            self.__animate()
        # right
        if (
            i < self.__num_cols - 1
            and not self.__cells[i][j].has_right_wall
            and not self.__cells[i + 1][j].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i + 1][j])
            self.__animate()
            if self.__solve_r(i + 1, j):
                self.path_length += 1
                return True
            self.__cells[i][j].draw_move(self.__cells[i + 1][j], undo=True)
            self.__animate()
        # up
        if (
            j > 0
            and not self.__cells[i][j].has_top_wall
            and not self.__cells[i][j - 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j - 1])
            self.__animate()
            if self.__solve_r(i, j - 1):
                self.path_length += 1
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j - 1], undo=True)
            self.__animate()
        # down
        if (
            j < self.__num_rows - 1
            and not self.__cells[i][j].has_bottom_wall
            and not self.__cells[i][j + 1].visited
        ):
            self.__cells[i][j].draw_move(self.__cells[i][j + 1])
            self.__animate()
            if self.__solve_r(i, j + 1):
                self.path_length += 1
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j + 1], undo=True)
            self.__animate()

        return False
            
