#!/usr/bin/env python

 - create_logger()
 - measurements_decorator(..)
 - fibonacci_memory(..)
 - print_statistics(..)
 - write_to_file(..)
"""

from pathlib import Path
from timeit import default_timer as timer
from functools import wraps
import argparse
import logging
import logging.config
import json

__version__ = '1.1'
__desc__ = "Program used for measuring execution time of various Fibonacci implementations!"

RESOURCES = Path(__file__).parent / "../_Resources/"

def create_logger() -> logging.Logger:
    """Create and return logger object."""
    pass  # TODO: Replace with implementation!


def measurements_decorator(func):
    """Function decorator, used for time measurements."""
    @wraps(func)
    def wrapper(nth_nmb: int) -> tuple:
        value_container = []
        t1 = timer()
        for i in range(0, nth_nmb):
            func_result = function(func)
            end_ = t1 - timer()
            print(
                f"Total execution time {func._name}: {end if end_ > 0 else 0} ms"
                )

    return wrapper
    #Pseudo Code for wrapper

# DEFINE list container for values
# MARK starttime
# LOG “Starting measurements...” at INFO level
# REPEAT IN RANGE nth_nmb - 0:
# DETERMINE fibonacci value AND add to container
# FOR EACH 5th iteration LOG information at DEBUG level
# MARK endtime AND calculate duration
# RETURN duration AND container AS tuple


@measurements_decorator
def fibonacci_iterative(nth_nmb: int) -> int:
    """An iterative approach to find Fibonacci sequence value.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    old, new = 0, 1
    if nth_nmb in (0, 1):
        return nth_nmb
    for __ in range(nth_nmb - 1):
        old, new = new, old + new
    return new

@measurements_decorator
def fibonacci_recursive(nth_nmb: int) -> int:
    """An recursive approach to find Fibonacci sequence value.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    def fib(_n):
        return _n if _n <= 1 else fib(_n - 1) + fib(_n - 2)
    return fib(nth_nmb)


@measurements_decorator
def fibonacci_memory(nth_nmb: int) -> int:
    memory_dict = {}
    if nth_nmb not in memory_dict:
        # Function definition
        def fib(_n):
            return _n if _n <= 1 else fib(_n - 1) + fib(_n - 2)
        # End of function definition
        memory_dict[nth_nmb] = fib(nth_nmb)
    else:
        return memory_dict[nth_nmb]
    print(memory_dict)


    # print("hello")
    # """An recursive approach to find Fibonacci sequence value, storing those already calculated."""
    # if (nth_nmb == 0):
    #     return 1;
    #     # recursion call
    # print("hello")
    # return nth_nmb * fibonacci_memory(nth_nmb)

fibonacci_memory(6)



def duration_format(duration: float, precision: str) -> str:
    """Function to convert number into string. Switcher is dictionary type here.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    switcher = {
        'Seconds': "{:.5f}".format(duration),
        'Milliseconds': "{:.5f}".format(duration * 1_000),
        'Microseconds': "{:.1f}".format(duration * 1_000_000),
        'Nanoseconds': "{:d}".format(int(duration * 1_000_000_000))
    }

    # get() method of dictionary data type returns value of passed argument if it is present in
    # dictionary otherwise second argument will be assigned as default value of passed argument
    return switcher.get(precision, "nothing")


def print_statistics(fib_details: dict, nth_value: int):
    """Function which handles printing to console."""
    line = '\n' + ("---------------" * 5)
    pass  # TODO: Replace with implementation!


def write_to_file(fib_details: dict):
    """Function to write information to file."""
    pass  # TODO: Replace with implementation!


def main():
    """The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    epilog = "DT179G Assignment 3 v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('nth', metavar='nth', type=int, nargs='?', default=30,
                        help="nth Fibonacci sequence to find.")

    global LOGGER  # ignore warnings raised from linters, such as PyLint!
    LOGGER = create_logger()

    args = parser.parse_args()
    nth_value = args.nth  # nth value to sequence. Will fallback on default value!

    fib_details = {  # store measurement information in a dictionary
        'fib iteration': fibonacci_iterative(nth_value),
        'fib recursion': fibonacci_recursive(nth_value),
        'fib memory': fibonacci_memory(nth_value)
    }

    print_statistics(fib_details, nth_value)    # print information in console
    write_to_file(fib_details)                  # write data files


if __name__ == "__main__":
    main()
