from util import Chromosome, GeneticAlgorithm, SelectionType
from random import shuffle, sample
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps

PEOPLE = ["Michael", "Sarah", "Joshua", "Narine", "David"
            "Sajid", "Melanie", "Daniel", "Wei", "Dean", "Brian", 
            "Murat", "Lisa"]

class ListCompression(Chromosome):
    def __init__(self, lst):
        self.lst = lst

    @property
    def bytes_compressed(self):
        return getsizeof(compress(dumps(self.lst)))

    def fitness(self):
        return 1 / self.bytes_compressed

    @classmethod
    def random_instance(cls):
        mylst = deepcopy(PEOPLE)
        shuffle(mylst)
        return ListCompression(mylst)

    def crossover(self, other):
        child1 = deepcopy(self)
        child2 = deepcopy(other)
        idx1, idx2 = sample(range(len(self.lst)), k = 2)
        l1, l2 = child1.lst[idx1], child2.lst[idx1]
        child1.lst[child1.lst.index(l2)], child1.lst[idx2] = child1.lst[idx2], l2
        child2.lst[child2.lst.index(l1)], child2.lst[idx1] = child2.lst[idx1], l1
        return child1, child2

    def mutate(self):
        idx1, idx2 = sample(range(len(self.lst)), k = 2)
        self.lst[idx1], self.lst[idx2] = self.lst[idx2], self.lst[idx1]

    def __str__(self):
        return f"Order: {self.lst} Bytes: {self.bytes_compressed}"


if __name__ == "__main__":
    initial_population = [ListCompression.random_instance() for _ in range(1000)]
    ga = GeneticAlgorithm(initial_population = initial_population, threshold = 1.0, max_generations = 1000,
                            mutation_chance = 0.2, crossover_chance = 0.7, selection_type = SelectionType.TOURNAMENT)
                            
    result = ga.run()
    print(result)