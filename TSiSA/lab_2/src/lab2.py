import random_search
import function
import numpy
import matplotlib.pyplot as plt


def plot_dots(dots):
    plt.scatter(*zip(*dots))
    plt.show()


function_unimodal = function.function
function_multimodal = function.function_multimodal
functions = (function_unimodal, function_multimodal)
a_border = -3.5
b_border = 3.5


def get_template_array(shape):
    return numpy.zeros(shape=shape)


def main():
    q_from, q_to, q_step = (0.005, 0.101, 0.005)
    q_values = numpy.arange(q_from, q_to, q_step)
    p_from, p_to, p_step = (0.90, 0.991, 0.01)
    p_values = numpy.arange(p_from, p_to, p_step)

    shape = (len(q_values), len(p_values))
    x_min_unimodal = get_template_array(shape)
    f_min_unimodal = get_template_array(shape)
    number_of_estimations_unimodal = get_template_array(shape)
    x_min_multimodal = get_template_array(shape)
    f_min_multimodal = get_template_array(shape)
    number_of_estimations_multimodal = get_template_array(shape)

    dots_total_unimodal = []
    dots_total_multimodal = []

    for i in range(len(q_values)):
        q = q_values[i]
        for j in range(len(p_values)):
            p = p_values[j]

            min_dot_unimodal, dots_unimodal = random_search.\
                random_search(function_unimodal, q, p, a_border, b_border)
            x_min_unimodal[i][j] = min_dot_unimodal[0]
            f_min_unimodal[i][j] = min_dot_unimodal[1]
            number_of_estimations_unimodal[i][j] = len(dots_unimodal)
            dots_total_unimodal.extend(dots_unimodal)

            min_dot_multimodal, dots_multimodal = random_search.\
                random_search(function_multimodal, q, p, a_border, b_border)
            x_min_multimodal[i][j] = min_dot_multimodal[0]
            f_min_multimodal[i][j] = min_dot_multimodal[1]
            number_of_estimations_multimodal[i][j] = len(dots_multimodal)
            dots_total_multimodal.extend(dots_multimodal)

    plot_dots(dots_total_multimodal)
    plot_dots(dots_total_unimodal)
    return



if __name__ == "__main__":
    main()