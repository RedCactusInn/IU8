
import function
function = function.function


def x_is_in_borders(x, a_border, b_border):
    if a_border > b_border:
        swap_tuple = (b_border, a_border)
        a_border, b_border = swap_tuple
    if a_border <= x <= b_border:
        return True
    return False


def find_minimum_optimal_passive_search(a_border: float, b_border: float, epsilon: float) -> tuple:
    function_in_a = function(a_border)
    function_in_b = function(b_border)

    current_x = a_border
    delta = epsilon
    first_dot = (a_border, function_in_a)
    if function_in_b < function_in_a:
        current_x = b_border
        delta = -epsilon / 2
        first_dot = (b_border, function_in_b)
    min_dot = first_dot
    dots = [first_dot]
    while True:
        current_x += delta
        if not x_is_in_borders(current_x, a_border, b_border):
            break
        previous_x, previous_f = dots[-1]
        current_f = function(current_x)

        if current_f > previous_f:
            break

        current_dot = (current_x, current_f)
        min_dot = current_dot
        dots.append(current_dot)

    return min_dot, dots


def find_minimum_passive_search(a_border: float, b_border: float, epsilon: float) -> tuple:
    x = a_border
    dots = []
    while x_is_in_borders(x, a_border, b_border):
        dots.append((x, function(x)))
        x += epsilon / 2
    x_min = min(dots, key=lambda elem: elem[1])
    return x_min, dots




