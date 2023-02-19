import random
import copy

class Generator:
    

    def __init__(self, dificulty):
        self.dificulty = dificulty
     

    """Generator sudoku mreze in resitve sudoku mreze"""



    '''Funkcija naredi novo re�itev sudokuja'''
    def generate(grid):
        newGrid = copy.deepcopy(grid)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(0, 81):
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

    '''Funkcija preveri, �e neko �tevilo v nekem polju ustreza pravilom sudokuja 
       glede na ostala �tevila v mre�i'''
    def isValid(grid, row, col, value):
        #Prevarjanje, �e se vrednost value ponovi v isti vrstici.
        for i in range(9):
            if grid[row][i] == value and i != col:
                return False
        #Preverjanje, �e se vrednost value ponovi v istem stolpcu.
        for i in range(9):
            if grid[i][col] == value and i != row:
                return False
        #Preverjanje, �e se vrednost value ponovi znotraj manj�ega kvadrata 3 x 3.
        for i in range(3):
            for j in range(3):
                if grid[i + (row // 3 * 3)][j + (col // 3 * 3)] == value and i != row and j != col:
                    return False
        return True

    def  removeNumbers(grid, difficulty):
        puzzle = [[]]
        puzzle = grid
        upperLimit = 0
        lowerLimit = 0
        #Dolo�i se spodnja in zgronja meja koliko polj se zbri�e v vrstici
        if difficulty == '1':
            upperLimit = 6
            lowerLimit = 4
        if difficulty == '2':
            upperLimit = 7
            lowerLimit = 5
        if difficulty == '3':
            upperLimit = 8
            lowerLimit = 6
        for i in range(9):
            level = random.sample(range(9), random.randint(lowerLimit,upperLimit))
            '''Seznam dolo�ene dol�ine �tevil od 1 do 9, 
            ki se ne ponavljajo in so naklju�no razporejena.'''
            level = random.sample(range(9), random.randint(lowerLimit,upperLimit))
            #Brisanje vrednosti v dolo�enem polju
            for j in level:
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
    
  









