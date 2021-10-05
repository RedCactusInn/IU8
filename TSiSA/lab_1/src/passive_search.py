
import function
function = function.function


def x_is_in_borders(x, a_border, b_border):
    if a_border > b_border:
        swap_tuple = (b_border, a_border)
        a_border, b_border = swap_tuple
    if a_border <= x <= b_border:
        return True
    return False


def find_minimum_passive_search(a_border: float, b_border: float, epsilon: float) -> tuple:
    x = a_border
    dots = []
    while x_is_in_borders(x, a_border, b_border):
        dots.append((x, function(x)))
        x += epsilon / 2
    min_dot = min(dots, key=lambda elem: elem[1])
    print(f"INFO: Number of estimations = {len(dots)}")
    x_min, y_min = min_dot
    print(f"INFO: Minimum found in x = {x_min}, y = {y_min}")
    return min_dot, dots




