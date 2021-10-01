import math

import function
function = function.function


def get_fibonacci_sequence(number_of_numbers: int) -> list:
    fibonacci_sequence = [0, 1]
    for index in range(number_of_numbers - 2):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence


def find_minimum_fibonacci_search(a_border: float, b_border: float, epsilon: float) -> tuple:
    number_of_iterations = math.ceil((b_border - a_border) / epsilon)
    fibonacci_sequence = get_fibonacci_sequence(number_of_iterations)
    print(number_of_iterations)

    coef_1 = fibonacci_sequence[-3] / fibonacci_sequence[-1]
    coef_2 = fibonacci_sequence[-2] / fibonacci_sequence[-1]

    x_1 = a_border + (b_border - a_border) * coef_1
    x_2 = a_border + (b_border - a_border) * coef_2
    y_1 = function(x_1)
    y_2 = function(x_2)

    dots = [(x_1, y_1), (x_2, y_2)]

    while True:
        if y_1 > y_2:
            a_border = x_1
            x_1 = x_2
            y_1 = y_2
            x_2 = b_border - (x_1 - a_border)
            y_2 = function(x_2)
            min_dot = (x_2, y_2)
        else:
            b_border = x_2
            x_2 = x_1
            y_2 = y_1
            x_1 = a_border + (b_border - x_2)
            y_1 = function(x_1)
            min_dot = (x_1, y_1)
        dots.append(min_dot)
        if number_of_iterations == 1:
            return min_dot, dots
        number_of_iterations -= 1




