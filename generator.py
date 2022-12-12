import random
import copy

class Generator:
    

    def __init__(self, dificulty):
        self.dificulty = dificulty
     
    """description of class"""

    def generate(grid):
        newGrid = copy.deepcopy(grid)
        for i in range(0, 81):
            numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            row = i // 9
            col = i % 9
            if newGrid[row][col] == 0:
                shuffledNumbers = random.sample(numbers, len(numbers))
                for num in shuffledNumbers:
                    if Generator.isValid(newGrid, row, col, num):
                        checkingGrid = copy.deepcopy(newGrid)
                        checkingGrid[row][col] = num
                        if Generator.solveSudoku(checkingGrid, 0, 0):
                            newGrid[row][col] = num
                            break
                        else:
                            continue
                    else:
                        continue
        return newGrid

    def solveSudoku(grid, row, col):
        if (row == 8 and col == 9):
            return True
        if col == 9:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return Generator.solveSudoku(grid, row, col + 1)
        for num in range(1, 10, 1):
            if Generator.isValid(grid, row, col, num):
                grid[row][col] = num
                if Generator.solveSudoku(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

    def isValid(grid, row, col, value):
        for i in range(9):
            if grid[row][i] == value and i != col:
                return False

        for i in range(9):
            if grid[i][col] == value and i != row:
                return False

        for i in range(3):
            for j in range(3):
                if grid[i + (row // 3 * 3)][j + (col // 3 * 3)] == value and i != row and j != col:
                    return False
        return True

    def  removeNumbers(grid, difficulty):
        puzzle = [[]]
        puzzle = grid
        for i in range(9):
            level1 = random.sample(range(9), random.randint(4,6))
            level2 = random.sample(range(9), random.randint(5,7))
            level3 = random.sample(range(9), random.randint(6,8))
            if difficulty == '1':
                for j in level1:
                    puzzle[i][j] = ' '
            if difficulty == '2':
                for j in level2:
                    puzzle[i][j] = ' '
            if difficulty == '3':
                for j in level3:
                    puzzle[i][j] = ' '
        return puzzle

    def generateSudoku(self):
        board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
        solution =  Generator.generate(board)
        solutionResult = copy.deepcopy(solution)
        grid =  Generator.removeNumbers(solution, self.dificulty)
        result = {
            'solution': solutionResult,
            'grid': grid
        }

        return result
    
  









