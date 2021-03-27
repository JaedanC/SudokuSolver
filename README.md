# Sudoku Solver 🧩

This Python script solves Sudoku's in the terminal using the backtracking method. I did this for fun without external resources. This may not be the most efficient way to solve them.

## Usage

You add Sudoku's manually by adding them to the `board_data` list. The example's can be removed if you wish.

## Data format

![Sudoku](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg/1200px-Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg.png)

This Sudoku from wikipedia is input into my solver by reading each row and writing the number that appears. Write gaps as a `0`.

For example, the above is:

`"530070000600195000098000060800060003400803001700020006060000280000419005000080079"`
