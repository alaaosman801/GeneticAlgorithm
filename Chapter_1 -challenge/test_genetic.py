import datetime
import unittest
import random
import genetic
import arabic_reshaper
from bidi.algorithm import get_display


def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(
        candidate.Genes, candidate.Fitness, str(timeDiff)))


class GuessPasswordTests(unittest.TestCase):
    geneset = " ضصثقفغعهخحجدشسيبلاتنمكطئءؤرلاىةوزظآلآإأ~ذ!.,@#$%^&*(){}[];:؟<>"

    def test(self):
        target = "امر أمير الآمراء بحرف بئر فى الصحراء كام راء فى ذلك؟"
        self.guess_password(target)

    def test1(self):
        target = "بسم الله الرحمن الرحيم"
        self.guess_password(target)

    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target),
                                optimalFitness, self.geneset, fnDisplay)
        self.assertEqual(best.Genes, target)

    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.geneset) for _ in
                         range(length))

        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(lambda: self.test_Random())

GuessPasswordTests().test()


