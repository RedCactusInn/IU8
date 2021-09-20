import matplotlib.pyplot as plt
import math
import time


def function(x: float):
    function_value = (1 - x) * (1 - x) + math.exp(x)
    return function_value


def x_is_in_borders(x, a_border, b_border):
    if a_border > b_border:
        swap_tuple = (b_border, a_border)
        a_border, b_border = swap_tuple
    if a_border <= x <= b_border:
        return True
    return False


def find_minimum_optimal_passive_search(a_border: float, b_border: float, epsilon: float) -> float:
    function_in_a = function(a_border)
    function_in_b = function(b_border)

    current_x = a_border
    delta = epsilon
    first_dot = (a_border, function_in_a)
    if function_in_b < function_in_a:
        current_x = b_border
        delta = -epsilon * 0.5
        first_dot = (b_border, function_in_b)
    x_min = current_x
    dots = [first_dot]
    while True:
        current_x += delta
        if not x_is_in_borders(current_x, a_border, b_border):
            break
        previous_x, previous_f = dots[-1]
        current_f = function(current_x)

        if current_f > previous_f:
            break

        x_min = current_x
        current_dot = (current_x, current_f)
        dots.append(current_dot)

    return x_min, dots


def plot_graph(f, a_border, b_border, step=0.1):
    x = a_border
    dots = []
    while x_is_in_borders(x, a_border, b_border):
        dots.append((x, f(x)))
        x += step

    plot_dots(dots)


def plot_dots(dots):
    plt.scatter(*zip(*dots))
    plt.show()


def main():
    delta_n = 0.05
    epsilon = 2 * delta_n
    a_border = -5.0
    b_border = 2.0

    x_min, dots = find_minimum_optimal_passive_search(a_border, b_border, epsilon)
    plot_dots(dots)
    plot_graph(function, a_border, b_border, step=0.1)


if __name__ == "__main__":
    timer_start = time.time()
    print(f"\nprogram has been started\n{'-' * 30}")
    main()
    timer_finish = time.time()
    print(f"{'-' * 30}\nprogram finished in {timer_finish - timer_start} seconds")
