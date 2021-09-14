# import matplotlib
import math
import time


def function(x: float):
    function_value = (1-x)*(1-x) + math.exp(x)
    return function_value


def find_minimum_optimal_passive_search(a_border: float, b_border: float, epsilon: float) -> float:
    number_of_dots = - 1 + (b_border - a_border) / epsilon
    dots = []
    current_x = a_border
    while current_x <= b_border:
        dot = (current_x, function(current_x))
        dots.append(dot)
        current_x += epsilon
    print(f"calculated number of dots: {number_of_dots}, real number of dots: {len(dots)}")


def main():
    epsilon = 0.1
    find_minimum_optimal_passive_search(-5.0, 2.0, epsilon)

if __name__ == "__main__":
    timer_start = time.time()
    print(f"\nprogram has been started\n{'-' * 30}")
    main()
    timer_finish = time.time()
    print(f"{'-' * 30}\nprogram finished in {timer_finish - timer_start} seconds")
