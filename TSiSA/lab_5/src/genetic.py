from population import Population
from individual import Individual


def _get_maximum(generations: list):
    pass


def find_maximum(fitness_function, domain: tuple, number_of_generations: int):
    generations = []
    population = Population.initial(number_of_individuals=4, bits_per_gene=10)
    generations.append(population.get_current_generation())
    for i in range(number_of_generations):
        population.set_domain(domain)
        population.set_fitness_function(fitness_function)
        population.evolve()
        generations.append(population.get_current_generation())
    maximum = _get_maximum(generations)
    return maximum, generations



