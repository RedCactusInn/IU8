import random_search
import function

function_unimodal = function.function
function_multimodal = function.function_multimodal
functions = (function_unimodal, function_multimodal)
a_border = -3.5
b_border = 3.5


def get_q_list():
    q_list = [
        0.005, 0.01,
        0.015, 0.02,
        0.025, 0.03,
        0.035, 0.04,
        0.045, 0.05,
        0.055, 0.06,
        0.065, 0.07,
        0.075, 0.08,
        0.085, 0.09,
        0.095, 0.1
    ]
    return q_list


def get_p_list():
    p_list = [
        0.90,
        0.91,
        0.92,
        0.93,
        0.94,
        0.95,
        0.96,
        0.97,
        0.98,
        0.99,
    ]
    return p_list


def main():
    for q in get_q_list():
        for p in get_p_list():
            for func in functions:
                min_dot, dots = random_search.random_search(func, q, p, a_border, b_border)




if __name__ == "__main__":
    main()