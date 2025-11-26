# 🎮 Stress Free Gaming - Maze Logic

## 🌟 Overview

**Maze Logic** is a Python-based application for generating and solving animated mazes. Utilizing the `tkinter` library for a graphical interface, this project visually demonstrates the use of **recursive backtracking** algorithms for both maze generation and solving.

It's a fantastic educational tool for visualizing graph traversal algorithms and a fun little game!


## ✨ Features

* **Customizable Maze Size:** Easily specify the number of rows and columns.
* **Animated Generation:** Watch the maze being constructed step-by-step using the **recursive backtracking algorithm** (Depth First Search variant).
* **Animated Solving:** Observe the path-finding process as the application solves the maze from entrance to exit.
* **Configurable Speed:** Adjust the animation speed or use a quick mode for instant results.
* **Seeding:** Use an optional random integer seed to generate the exact same maze every time.

## 🛠️ Installation

This project requires Python 3.x and the built-in `tkinter` library.

1.  **Clone the repository:**
    ```bash
    git clone [Your-Repo-Link-Here]
    cd maze-logic
    ```

2.  **Ensure all files are present:**
    Make sure the following files are in your project directory:
    * `main.py`
    * `maze.py`
    * `cell.py`
    * `graphics.py`
    * `config.py`

## 🚀 Usage

Run the main application file from your terminal:

```bash
python main.py
```

### Command Line Arguments

You can customize the maze generation and behavior using various command-line arguments:

| Argument | Description | Default Value | Example |
| :--- | :--- | :--- | :--- |
| -C <columns> | Set the number of **columns** for the maze. | 16 | python main.py -C 30 |
| -R <rows> | Set the number of **rows** for the maze. | 10 | python main.py -R 20 |
| -S <seed> | Set an **integer random seed** for repeatable mazes. | Random | python main.py -S 42 |
| -Q | **Quick mode:** Disables all animations for instant generation and solving. | Animated (0.05s) | python main.py -Q |
| -NS | **No Solve:** Generates the maze but skips the auto-solve step. | Auto-Solve (True) | python main.py -NS |
| --help or -h | Display the usage guide. | - | python main.py --help |

---

## 📐 Implementation Details

### Maze Generation

The maze is generated using a **Depth-First Search (DFS) variant** known as the **Recursive Backtracker** algorithm, implemented in the __break_walls_r method within maze.py.

1.  Start at a cell and mark it as visited.
2.  While the current cell has unvisited neighbors:
    a. Randomly choose one unvisited neighbor.
    b. **Knock down the wall** between the current cell and the chosen neighbor.
    c. Recursively call the function on the neighbor.
3.  If there is nowhere to go, **backtrack** to the previous cell.

The maze entrance is created by removing the top wall of the cell at (0, 0), and the exit by removing the bottom wall of the cell at (num_cols - 1, num_rows - 1).

### Maze Solving

The maze is solved immediately after generation using another **Recursive Backtracking** process, implemented in __solve_r in maze.py.

1.  Start at the entrance (top-left cell) and mark it as visited.
2.  If the exit (bottom-right cell) is reached, the path is found and returns True.
3.  For each available non-wall, unvisited neighbor:
    a. Draw a move line (in **Red**) to the neighbor using draw_move.
    b. Recursively call the function on the neighbor.
    c. If the recursive call returns True, the exit was found, propagate the True result.
    d. If the recursive call returns False (dead end), **backtrack** by drawing an undo line (in **Grey**) and return False.

The visual drawing of moves between cell centers is handled by the draw_move method in cell.py.

---

## ⚙️ Project Structure

| File | Role | Key Components/Functionality |
| :--- | :--- | :--- |
| main.py | **Entry Point** | Handles command-line arguments, sets maze parameters, initializes the Window and Maze. |
| maze.py | **Maze Logic** | Maze class: manages cell grid, implements __break_walls_r (generation) and __solve_r (solving). |
| cell.py | **Cell Logic** | Cell class: tracks wall status (top, bottom, left, right), handles drawing the walls and drawing moves (draw_move). |
| graphics.py | **Graphics/Drawing** | Window, Point, and Line classes: interfaces with tkinter to handle canvas and drawing lines. |
| config.py | **Configuration** | Static values for screen dimensions, margin, and various drawing colours (e.g., PATH_COLOUR, UNDO_COLOUR). |

---

## 🎨 Configuration

You can easily modify the look and feel of the maze by editing the static values in config.py:

```python
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MARGIN = 50

BACKGROUND_COLOUR = "white" # Background color for the canvas
MAZE_COLOUR = "black"       # Color for cell walls
PATH_COLOUR = "red"         # Color for successful moves
UNDO_COLOUR = "grey"        # Color for backtracking moves
```

---

## 🐛 Known Issues
High numbers of rows and columns results in RecursionError: maximum recursion depth exceeded.

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions for new features, bug fixes, or performance improvements.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.