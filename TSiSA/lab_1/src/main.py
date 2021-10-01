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

    # min_dot, dots = passive_search.find_minimum_optimal_passive_search(a_border, b_border, epsilon)
    # min_dot, dots = passive_search.find_minimum_passive_search(a_border, b_border, epsilon)
    min_dot, dots = fibonacci_search.find_minimum_fibonacci_search(a_border, b_border, epsilon)

    x_min, y_min = min_dot
    print(f"INFO: minimum found in x = {x_min}, f({x_min}) = {y_min}")
    plot_dots(dots)


if __name__ == "__main__":
    timer_start = time.time()
    print(f"\nprogram has been started\n{'-' * 30}")
    main()
    timer_finish = time.time()
    print(f"{'-' * 30}\nprogram finished in {timer_finish - timer_start} seconds")
