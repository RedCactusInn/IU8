import matplotlib.pyplot as plt
import time
import passive_search
import fibonacci_search


def plot_dots(dots):
    plt.scatter(*zip(*dots))
    plt.show()


def main():

    epsilon = 0.1
    a_border = -5.0
    b_border = 2.0

    methods = (
        fibonacci_search.find_minimum_fibonacci_search,
        passive_search.find_minimum_passive_search
    )
    for method in methods:
        tic = time.perf_counter()
        print(f"\n=== Computations started\n{'-' * 30}")
        min_dot, dots = method(a_border, b_border, epsilon)
        toc = time.perf_counter()
        print(f"{'-' * 30}\n=== Computations finished in {toc - tic} seconds")

    plot_dots(dots)


if __name__ == "__main__":

    main()

