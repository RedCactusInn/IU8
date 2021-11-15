import genetic
from fitness_function import fitness_function


def main():
    domain = ((-2, 2), (-2, 2))
    maximum, generations = genetic.find_maximum(fitness_function, domain, number_of_generations = 100)


if __name__ == "__main__":
    main()