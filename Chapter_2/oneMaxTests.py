import datetime
import unittest
import random
import genetic

def get_fitness(genes):
    return genes.count(1)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}...{1}\t{2:3.2f}\t{3}".format(''.join(map(str, candidate.Genes[:15])),
    ''.join(map(str, candidate.Genes[-15:])),
    candidate.Fitness,str(timeDiff)))


class OneMaxTests(unittest.TestCase):
    

    def test(self, length=1000):
        geneset = [0, 1]
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = length
        best = genetic.get_best(fnGetFitness, length,
                                optimalFitness, geneset, fnDisplay)
        self.assertEqual(best.Fitness, optimalFitness)


    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test(4000))

OneMaxTests().test()

