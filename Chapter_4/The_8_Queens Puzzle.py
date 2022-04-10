import unittest
import datetime
import genetic


def get_fitness(genes, size):
    board = Board(genes, size)
    rowsWithQueens = set()
    colsWithQueens = set()
    northEastDiagonalWithQueens = set()
    southEastDiagonalWithQueens = set()
    for row in range(size):
        for col in range(size):
          if board.get(row, col) == 'Q':
              rowsWithQueens.add(row)
              colsWithQueens.add(col)
              northEastDiagonalWithQueens.add(row+col)
              southEastDiagonalWithQueens.add(size - 1 - row+col)

    Qnum = len(rowsWithQueens)+ \
               len(colsWithQueens)+ \
                len(northEastDiagonalWithQueens) \
                    + len(southEastDiagonalWithQueens)
    total = size - Qnum
    return Fitness(total)




def display(candidate, startTime, size):
    timeDiff = datetime.datetime.now() - startTime
    board = Board(candidate.Genes, size)
    board.print()
    print("{0}\t - {1}\t{2}".format(
        ' '.join(map(str, candidate.Genes)),
        candidate.Fitness,
        str(timeDiff)
    ))


class _8Queens(unittest.TestCase):
    def Qtest(self, size = 8):
        geneset = [i for i in range(size)]
        startTime = datetime.datetime.now()
        
        def Display(candidate):
            display(candidate, startTime, size)

        def GetFitness(genes):
            return get_fitness(genes, size)

        optimalFitness = Fitness(0)
        best = genetic.get_best(GetFitness, 2*size,
                                 optimalFitness, geneset, Display )

        self.assertTrue(not optimalFitness > best.Fitness)
    
    def test_benchmark(self):
         genetic.Benchmark.run(lambda: self.Qtest(200))



class Board:
    def __init__(self, genes, size):
        board = [['.']*size for _ in range(size)]
        for idx in range(0, len(genes), 2):
            row = genes[idx]
            col = genes[idx + 1]
            board[col][row] = 'Q'
        self._board = board


    def get(self, row, col):
        return self._board[col][row]

    def print(self):
        for i in reversed(range(len(self._board))):
            print(' '.join(self._board[i])) 


class Fitness:
    total = None

    def __init__(self, total):
        self.total = total

    def __gt__(self, other):
        return self.total < other.total

    def __str__(self):
        return "{0}".format(self.total)    
  


_8Queens().Qtest()