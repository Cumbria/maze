import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )

        print(f"\nExpect : {num_cols} columns")
        print(f"Actual : {len(m1._Maze__cells)} columns")

        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

        print(f"\nExpect : {num_rows} rows")
        print(f"Actual : {len(m1._Maze__cells[0])} columns")


    def test_maze_create_more_cells(self):
        num_cols = 20
        num_rows = 16
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._Maze__cells),
            num_cols,
        )

        print(f"\nExpect : {num_cols} columns")
        print(f"Actual : {len(m2._Maze__cells)} columns")

        self.assertEqual(
            len(m2._Maze__cells[0]),
            num_rows,
        )

        print(f"\nExpect : {num_rows} rows")
        print(f"Actual : {len(m2._Maze__cells[0])} columns")

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall,
            False,
        )


if __name__ == "__main__":
    unittest.main()
