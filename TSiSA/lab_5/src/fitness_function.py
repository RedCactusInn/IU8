import math
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fitness_function(x, y):
    return math.cos(x) * math.cos(y)