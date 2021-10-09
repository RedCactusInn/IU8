import math

import function
function = function.function


class FibonacciSequence:

    _sequence = []

    def __init__(self, length: int = 10):
        self._sequence = [1, 1]
        self.extend_to_length(length)

    def extend_to_length(self, length: int) -> list:
        assert (len(self._sequence) > 1)
        while len(self._sequence) < length:
            self._sequence.append(self._sequence[-1] + self._sequence[-2])

    def lengthen_by(self, number_of_elements: int):
        for i in range(number_of_elements):
            self._sequence.append(self._sequence[-1] + self._sequence[-2])

    def get_sequence(self):
        return self._sequence


def get_number_of_iterations(low_border):
    fibonacci_sequence = FibonacciSequence()
    while fibonacci_sequence.get_sequence()[-1] < low_border:
        fibonacci_sequence.lengthen_by(1)
    return len(fibonacci_sequence.get_sequence())


def find_minimum_fibonacci_search(a_border: float, b_border: float, epsilon: float) -> tuple:
    low_border = math.ceil((b_border - a_border) / epsilon)
    number_of_iterations = get_number_of_iterations(low_border)

    fibonacci_sequence = FibonacciSequence(number_of_iterations).get_sequence()

    x_1 = a_border + (b_border - a_border) * fibonacci_sequence[-3] / fibonacci_sequence[-1]
    x_2 = a_border + (b_border - a_border) * fibonacci_sequence[-2] / fibonacci_sequence[-1]
    y_1 = function(x_1)
    y_2 = function(x_2)

    dots = [(x_1, y_1), (x_2, y_2)]

    for i in range(number_of_iterations):
        if y_1 > y_2:
            a_border = x_1
            x_1 = x_2
            y_1 = y_2
            x_2 = b_border - (x_1 - a_border)
            y_2 = function(x_2)
            dots.append((x_2, y_2))
            continue
        b_border = x_2
        x_2 = x_1
        y_2 = y_1
        x_1 = a_border + (b_border - x_2)
        y_1 = function(x_1)
        dots.append((x_1, y_1))
    min_dot = (x_2, y_2) if y_2 < y_1 else (x_1, y_1)

    print(f"INFO: Number of estimations = {len(dots)}")
    x_min, y_min = min_dot
    print(f"INFO: Minimum found in x = {x_min}, y = {y_min}")
    return min_dot, dots

