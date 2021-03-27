class SudokuSolver:
    class Move:
        def __init__(self, tile):
            if tile.get_number() is not None:
                raise ValueError("Moves can only be done to tiles with no number")

            self.tile = tile

        def get_tile(self):
            return self.tile
        
        def next_number(self):
            current_number = self.tile.get_number()

            if current_number is None:
                self.tile.set_number(1)
                return True
            
            current_number += 1
            if current_number > 9:
                self.tile.set_number(None)
                return False
            self.tile.set_number(current_number)
            return True
        
        def reset(self):
            self.tile.set_number(None)

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.moves = []

        for tile in sudoku:
            if tile.get_number() is None:
                self.moves.append(self.Move(tile))

    def solve(self):
        """
        This is solved using the backtracking technique
        """
        if not self.sudoku.is_currectly_correct():
            print("The Sudoku is not possible to solve from initial values")
            return None

        counter = 0
        # iterations = 0
        while True:
        # while iterations < 4:
            # if iterations % 10000 == 0:
            #     print(iterations, self.sudoku)
            # iterations += 1

            # Check if we found a solution, or can't find a solution
            if counter >= len(self.moves):
                return self.sudoku
            elif counter < 0:
                print("The Sudoku is not possible to solve")
                return None
            
            current_move = self.moves[counter]
            if current_move.next_number():
                row = current_move.get_tile().get_row()
                col = current_move.get_tile().get_col()
                square = (row // 3, col // 3)

                groups = [
                    self.sudoku.get_row(row),
                    self.sudoku.get_col(col),
                    self.sudoku.get_square(*square)
                ]

                # print(groups)

                # Is this move legit?
                results = [Sudoku.is_grouping_possible(group) for group in groups]

                # No. Try a new number
                if False in results:
                    continue

                # Yes. Try the next number
                counter += 1
            else:
                # This move is invalid with all numbers [1-9]
                counter -= 1
                continue


class Sudoku:
    @staticmethod
    def is_grouping_possible(group):
        numbers = list(map(lambda tile: tile.get_number(), group))
        numbers_no_none = list(filter(lambda n: n is not None, numbers))
        numbers_no_dups = set(numbers_no_none)
        return len(numbers_no_none) == len(numbers_no_dups)

    class Tile:
        def __init__(self, row, col, number):
            self.row = row
            self.col = col
            if number == "0":
                self.number = None
            else:
                self.number = int(number)
            

        def __repr__(self):
            if self.number is None:
                return " "
            return str(self.number)
        
        def set_number(self, number):
            self.number = number
            return self

        def get_number(self):
            return self.number
        
        def get_row(self):
            return self.row
        
        def get_col(self):
            return self.col

    def __init__(self, tile_data):
        self.tiles = [[None for __ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                number = tile_data[(row * 9) + col]
                self.tiles[row][col] = self.Tile(row, col, number)
    
    def __str__(self):
        horizontal_line = "-" * ((3 * 5) + 4) + "\n"
        output = ""
        for i, row in enumerate(self.tiles):
            if ((i+0) % 3 == 0):
                output += horizontal_line

            output += "|"
            for j in range(9):
                if ((j+1) % 3 == 0):
                    output += str(row[j]) + "|"
                else:
                    output += str(row[j]) + " "
            output += "\n"
        output += horizontal_line
        return output
    
    def __iter__(self):
        self.iter = 0
        return self

    def __next__(self):
        if (self.iter >= 9 * 9):
            raise StopIteration
        row = self.iter // 9
        col = self.iter % 9
        tile = self.tiles[row][col]
        self.iter += 1
        return tile
    
    def get_row(self, index):
        if (index < 0 or index >= 9):
            raise IndexError
        
        return self.tiles[index]
    
    def get_col(self, index):
        if (index < 0 or index >= 9):
            raise IndexError
        
        col = []
        for row in self.tiles:
            col.append(row[index])
        return col
    
    def get_square(self, row, col):
        if (row < 0 or row >= 3):
            raise IndexError
        if (col < 0 or col >= 3):
            raise IndexError
        
        square = []
        for i in range(3 * row, 3 * row + 3):
            for j in range(3 * col, 3 * col + 3):
                square.append(self.tiles[i][j])
        return square
    
    def is_currectly_correct(self):
        all_groups = []
        for i in range(9):
            all_groups.append(game.get_row(i))
            all_groups.append(game.get_col(i))

        for i in range(3):
            for j in range(3):
                all_groups.append(game.get_square(i, j))
        
        results = [Sudoku.is_grouping_possible(group) for group in all_groups]
        return False not in results
    

if __name__ == "__main__":
    board_data = [
        "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
        "534070000627195000198000060800060003400803001700020006060000280000419005000080079",
        "110000000000000000000000000000000000000000000000000000000000000000000000000000000",
        "300000009000070102000009500070050000100400680006000000710090005000003800400000020",
        "000092370800000000060800400700000832090000005000500100006001000030060050005007000",
        "000000000000000000000000000000000000000000000000000000000000000000000000000000001"
    ]
    
    for i, data in enumerate(board_data):
        print("Game #{}".format(i + 1))
        game = Sudoku(data)
        print("Board:")
        print(game)
        print("Solution:")
        print(SudokuSolver(game).solve())
        print("--------------------------------------------------------------------")