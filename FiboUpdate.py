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

def create_logger() -> logging.Logger:
    """Create and return logger object."""
    logging.basicConfig(level=logging.DEBUG, filename='sample.log')
    logger = logging.getLogger()
    configuration_file = str(RESOURCES) + "\\ass3_log_conf.json"

    with codecs.open(configuration_file, 'r', encoding='utf-8') as file:
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

    # get() method of dictionary data type returns value of passed argument if it is present in
    # dictionary otherwise second argument will be assigned as default value of passed argument
    return switcher.get(precision, "nothing")

def print_statistics(fib_details: dict, nth_value: int):
    """Function which handles printing to console."""
    line = '\n' + ("---------------" * 5)
    print(line)
    print("\n\t Duration between each interval: " + str(nth_value) + '-0')
    print(line)
    print("{0}\t\t\t\t {1:<7}\t {2:<7}\t {3:<7}\t {4:<7}".format("", "seconds", "milliseconds", "microseconds",
                                                                 "nanoseconds"))

    for detail in fib_details:
        print("{0}\t\t\t\t {1:<7}\t {2:<13}\t {3:<13}\t {4:<7}".format(detail,
                                                                       duration_format(fib_details[detail][0],
                                                                                       "Seconds"),
                                                                       duration_format(fib_details[detail][0],
                                                                                       "Milliseconds"),
                                                                       duration_format(fib_details[detail][0],
                                                                                       "Microseconds"),
                                                                       duration_format(fib_details[detail][0],
                                                                                       "Nanoseconds")
                                                                       ))

def write_to_file(fib_details: dict):
    """Function to write information to file."""
    for detail in fib_details:
        resource_path = str(Path(RESOURCES))
        with open(resource_path + "\\" + detail + ".txt", 'w+') as file:
            for idx, value in zip(range(len(fib_details[detail][1]) - 1, -1, -1), fib_details[detail][1].values()):
                file.write("{}: {}\n".format(idx, value))


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
