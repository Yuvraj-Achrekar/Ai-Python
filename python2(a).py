class QueenChessBoard:
    def __init__(self, size):
        # board has dimension size x size
        self.size = size
        # columns[r] is as number c if a queen is placed at row r and column c.
        # columns[r] is out of range if no queen is place fin row r
        self.columns = []
    def place_in_next_row(self, column):
        self.columns.append(column)
    def remove_in_current_row(self):
        return self.columns.pop()
    def is_this_column_safe_in_next_row(self, column):
        row = Len(self.columns)
        for queen_column in self.columns:
            if column == queen_column:
                return False
        for queen_row, queen_cloumn in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
        for queen_row, queen_cloumn in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
            return True
        def display(self):
            for row in range(self.size):
                for column in range(self.size):
                    if column == self.columns[row]:
                        print('Q', end=' ')
                    else:
                        print('.', end=' ')
                print()
        def solve_queen (size):
            """Display a chessboard for each possible configuration of placing n queens on an n x n chessboard and pr"""
            board = QueenChessBoard(size)
            number_of_solutions = 0
            row = 0
            column = 0
            while True:
                    while column < size:
                        if board.is_this_column_safe_in_next_row(column):
                            board.place_in_next_row(column)
                            row += 1
                            column = 0
                            break
                        else:
                            column += 1
            if (column == size or row == size):
                if row == size:
                    board.display()
                    print()
                    number_of_solutions += 1
                    board.remove_in_current_row()
                    row -= 1
                    try:
                        prev_column = board.remove_in_current_row()
                    except IndexError:
                       row -= 1
                       column = 1 + prev_column
            print('Number of solutins:', numbr_of_solutions)
    n = int(input('Enter n: '))
    solve_queen(n)

                    
                    
