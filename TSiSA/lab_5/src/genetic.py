from population import Population
from individual import Individual


def find_maximum(fitness_function, domain: tuple, number_of_generations: int):
    generations = []
    population = Population.initial(number_of_individuals=40, bits_per_gene=10)
    generations.append(population.get_current_generation())
    for i in range(number_of_generations):
        population.set_domain(domain)
        population.set_fitness_function(fitness_function)
        population.evolve()
        generations.append(population.get_current_generation())
    maximum = max([individual.get_fitness(fitness_function, domain) for individual in generations[-1]])
    return maximum, generations

