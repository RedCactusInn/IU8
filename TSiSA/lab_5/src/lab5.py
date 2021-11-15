import genetic
from fitness_function import fitness_function


def main():
    domain = ((-2, 2), (-2, 2))
    maximum, generations = genetic.find_maximum(fitness_function, domain)


if __name__ == "__main__":
    main()