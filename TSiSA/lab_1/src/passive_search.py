import matplotlib
import math
import time


def function(x: float):
    function_value = (1-x)*(1-x) + math.exp(x)
    return function_value


def find_minimum


def main():
    print(function(1))


if __name__ == "__main__":
    timer_start = time.time()
    print(f"\nprogram has been started\n{'-' * 30}")
    main()
    timer_finish = time.time()
    print(f"{'-' * 30}\nprogram finished in {timer_finish - timer_start} seconds")
