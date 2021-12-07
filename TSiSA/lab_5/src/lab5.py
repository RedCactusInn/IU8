import genetic
from fitness_function import fitness_function
from matplotlib import pyplot as plt
import individual
import random


def unpack_generation(generation: list, domain: tuple):
    dots = []
    for species in generation:
        x, y = species.decode_chromosome(domain)
        dots.append((x, y))
    return dots


def plot_generations(generations: list, domain: tuple):
    decrements = (0x010000, 0x000001, 0x000100)
    col = 0x101010
    for generation in generations:
        dots = unpack_generation(generation, domain)
        plt.plot([x for x, y in dots], [y for x, y in dots],
                 color=f"#{hex(col)[2:]}", marker='o',
                 linewidth=0)
        col += decrements[random.randint(0, 2)]
    plt.show()


def main():
    domain = ((-2, 2), (-2, 2))
    maximum, generations = genetic.find_maximum(fitness_function, domain,
                                                number_of_generations=600)
    print(f'maximum: {maximum}')
    plot_generations(generations, domain)


if __name__ == "__main__":
    main()
