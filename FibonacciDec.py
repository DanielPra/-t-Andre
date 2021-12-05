#!/usr/bin/env python

""" DT179G - LAB ASSIGNMENT 3
You find the description for the assignment in Moodle, where each detail regarding requirements
are stated. Below you find the inherent code, some of which fully defined. You add implementation
for those functions which are needed:

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
import codecs

__version__ = '1.1'
__desc__ = "Program used for measuring execution time of various Fibonacci implementations!"

RESOURCES = Path(__file__).parent / "../_Resources/"

#I rewrote create_logger so it will be OS agnostic and can be used in either
# Windows or Linux

def create_logger() -> logging.Logger:
    """Create and return logger object."""
    logger = logging.getLogger()
    configuration_file = RESOURCES / "ass3_log_conf.json"
    with open(configuration_file, 'r', encoding='utf-8') as file:
        config = json.load(file)
    logging.config.dictConfig(config=config)
    logger = logging.getLogger('ass_3_logger')
    return logger


def measurements_decorator(func):
    """Function decorator, used for time measurements."""
    @wraps(func)
    def wrapper(nth_nmb: int) -> tuple:
        value_container = {}  # Defining the list container for values
        start = timer()  # Saving the start time just before calling the function.
        LOGGER.info("Starting measurements...")
        for i in reversed(range(nth_nmb + 1)):
            value_container[i] = func(i)
            if i % 5 == 0:  # For every 5th iteration log info at Debug Level
                LOGGER.debug(str(i) + str(value_container[i]))
                #LOGGER.info("%s: %s",i ,value_container[i])
        duration = timer() - start
        return duration, value_container
    return wrapper

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


# I did read your comments regarding fibonacci_memory. I left it as is as it
# was your code and not mine, but I get your point. but I can see how your
# version would be a better option.

@measurements_decorator
def fibonacci_memory(nth_nmb: int) -> int:
    memory_dict = {0: 0, 1: 1}

    # Function definition
    def fib(_n):
        if _n not in memory_dict:
            memory_dict[_n] = fib(_n - 1) + fib(_n - 2)
        return memory_dict[_n]

    # End of function definition
    return fib(nth_nmb)


def duration_format(duration: float, precision: str) -> str:
    """Function to convert number into string. Switcher is dictionary type here.
    YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!"""
    switcher = {
        'Seconds': "{:.5f}".format(duration),
        'Milliseconds': "{:.5f}".format(duration * 1_000),
        'Microseconds': "{:.1f}".format(duration * 1_000_000),
        'Nanoseconds': "{:d}".format(int(duration * 1_000_000_000))
    }
    return switcher.get(precision, "nothing")

def print_statistics(fib_details: dict, nth_value: int):
    """Function which handles printing to console."""
    line = '\n' + ("---------------" * 5)
    print(line)
    format_row = "{:>13}" * (1 + 1)
    MSG=f"DURATION FOR EACH APPROACH WITHIN INTERVAL: {nth_value}-0"
    print(format_row.format("", MSG))
    print(("---------------" * 5))
    approaches = fib_details.keys() # Iterative, recursive...
    timings=['Seconds','Milliseconds','Microseconds','Nanoseconds']
    durations=prepare_table_content(fib_details,timings)
    ## we start with the first row which is the different timings
    format_row = "{:>13}" * (len(timings) + 1)
    print(format_row.format("", *timings))
    for approach, dur in zip(approaches, durations):
        print(format_row.format(approach, *dur))


def prepare_table_content(fib_details: dict, timings):
    # we will calculate different durations for each timing
    durations = []
    for _,value in fib_details.items():
        duration,_=value
        sub_durations=[]
        # for each timing we calculate the durations
        for timing in timings:
            sub_durations.append(duration_format(duration,timing))
        durations.append(sub_durations)
    return durations


def write_to_file(fib_details: dict):
    """Function to write information to file."""
    for approach, details in fib_details.items():
        # here we replace the spaces in approach name with "_" to use it as a filename
        FILE_NAME=approach.replace(" ","_") + ".txt"
        f = open(RESOURCES / FILE_NAME , "w")
        _, fibo_dict=details
        for number, fibo_n in fibo_dict.items():
            f.write(str(number)+": "+str(fibo_n)+"\n")
        f.close()


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
