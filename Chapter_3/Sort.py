'''
generate 10 sorted numbers in accending 
sequential => count of number in accending order
Gap => differance between gene[i-1] and gene[i]
totalGap => the summation of all gaps in the chromosome
'''
import datetime
import unittest
import genetic

#sort the array in accending order

class Fitness:
    NumberInSequenceCount = None
    TotalGap = None

    def __init__(self, NumberInSequenceCount, totalGap):
        self.NumberInSequenceCount  = NumberInSequenceCount
        self.TotalGap = totalGap

    def __gt__(self, other):
        if self.NumberInSequenceCount != other.NumberInSequenceCount:
            return self.NumberInSequenceCount > other.NumberInSequenceCount
        return self.TotalGap < other.TotalGap

    def __str__(self):
        return "{0} Sequential, {1} Total Gap".format(self.NumberInSequenceCount,self.TotalGap)




# calculate Fitness and gaps
def get_fitness(genes):
    fitness = 1
    gap = 0
    for i in range (1, len(genes)):
        if genes[i] > genes[i-1]:
            fitness +=1
        else:
            gap+= genes[i-1] - genes[i]
    return Fitness(fitness, gap)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t=> {1}\t{2}".format(
        ', '.join (map (str, candidate.Genes)), candidate.Fitness, str(timeDiff)))

class SortNumbersTests(unittest.TestCase):
    
    def test_sort_numbers(self):
        self.sort_numbers(10)
    
    def sort_numbers(self,totalNumbers):
        geneset = [i for i in range(100)]
        startTime = datetime.datetime.now()

        def Display(candidate):
            display(candidate, startTime)

        def getFitness(genes):
            return get_fitness(genes)

        optimalFitness = Fitness(totalNumbers, 0)
        best = genetic.get_best(getFitness, totalNumbers,optimalFitness,geneset,Display)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.sort_numbers(40))






SortNumbersTests().test_sort_numbers()