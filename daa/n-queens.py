class NQueens:
    def __init__(self) -> None:
        self.size = int(input("Enter size of chessboard: "))
        self.board = [[False]*self.size for _ in range(self.size)]
        self.count = 0

    def printBoard(self):
        for row in self.board:
            print(" ".join("Q" if cell else "X" for cell in row))
        print()

    def isSafe(self, row: int, col: int) -> bool:
        # Check the column and diagonals for attacks
        for i in range(row):
            if self.board[i][col] or (col - (row - i) >= 0 and self.board[i][col - (row - i)]) or (col + (row - i) < self.size and self.board[i][col + (row - i)]):
                return False
        return True

    def set_position_first_queen(self):
        while True:
            try:
                print("Enter coordinates of the first queen: ")
                row = int(input(f"Enter row (1-{self.size}): ")) - 1
                col = int(input(f"Enter column (1-{self.size}): ")) - 1
                if 0 <= row < self.size and 0 <= col < self.size:
                    self.board[row][col] = True
                    self.printBoard()
                    break
                else:
                    print("Coordinates are out of bounds. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")

    def solve(self, row: int):
        if row == self.size:
            self.count += 1
            self.printBoard()
            return
        
        if any(self.board[row]):  # Skip row if a queen is already placed
            self.solve(row + 1)
            return

        for col in range(self.size):
            if self.isSafe(row, col):
                self.board[row][col] = True
                self.solve(row + 1)
                self.board[row][col] = False

    def displayMessage(self):
        if self.count > 0:
            print(f"Solution exists for the given position of the queen: {self.count} solution(s) found.")
        else:
            print("Solution doesn't exist for the given position of the queen.")

# Running the solver
solver = NQueens()
solver.set_position_first_queen()
solver.solve(0)
solver.displayMessage()
