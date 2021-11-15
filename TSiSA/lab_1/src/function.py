import math


def function(x: float) -> float:
    function_value = (1 - x) * (1 - x) + math.exp(x)
    return function_value


def function_multimodal(x: float) -> float:
    return function(x) * math.sin(5 * x)
