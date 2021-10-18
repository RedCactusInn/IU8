import random
import math


def get_number_of_estimations(p, q) -> int:
    number_of_estimations = math.ceil(math.log(1 - p) / math.log(1 - q))
    return number_of_estimations


def random_search(func, q, p, a_border, b_border) -> tuple:
    a_border, b_border = (a_border, b_border) if b_border > a_border else (b_border, a_border)
    area = b_border - a_border
    number_of_estimations = get_number_of_estimations(p, q)
    dots = []
    for estimation in range(number_of_estimations):
        x = (random.random()) * area + a_border
        y = func(x)
        dots.append((x, y))
    min_dot = min(dots, key=lambda elem: elem[1])
    return min_dot, dots

