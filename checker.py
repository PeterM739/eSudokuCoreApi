
class Checker:
    """description of class"""

    def checkSolution(checkGrid, solutionGrid):
        for i in range(0,9):
            for j in range(0,9):
                if solutionGrid[i][j] == ' ':
                    return 0
                else :
                    if solutionGrid[i][j] != checkGrid[i][j]:
                        return 1
                    else:
                        continue
        return 2



