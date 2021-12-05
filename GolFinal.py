import argparse
import random
import json
import logging
import itertools
from pathlib import Path
from ast import literal_eval
from time import sleep

import code_base as cb

__version__ = '1.0'
__desc__ = "A simplified implementation of Conway's Game of Life."

RESOURCES = Path(__file__).parent / "../_Resources/"


# -----------------------------------------
# IMPLEMENTATIONS FOR HIGHER GRADES, C - B
# -----------------------------------------

def load_seed_from_file(_file_name: str) -> tuple:
    """ Load population seed from file. Returns tuple: population (dict) and world_size (tuple). """
    pass


def create_logger() -> logging.Logger:
    """ Creates a logging object to be used for reports. """
    pass


def simulation_decorator(func):
    """ Function decorator, used to run full extent of simulation. """
    pass


# -----------------------------------------
# BASE IMPLEMENTATIONS
# -----------------------------------------

def parse_world_size_arg(_arg: str) -> tuple:
    """ Parse width and height from command argument. """
    try:
        split_list = [int(item) for item in _arg.split("x")]
        if len(split_list) != 2:
            raise AssertionError("World size should contain width and height, Ex: '80x40'")
        for value in split_list:
            #Check if below 1
            if value < 1:
                raise ValueError("Both width and height needs to have positive values above zero.")
        return tuple(split_list)
    except Exception as e:
        print(e)
        print("Using default world size: 80x40")
        world_size = (80,40)
        return world_size

def calc_neighbour_positions(_cell_coord: tuple) -> list:
    """ Calculate neighbouring cell coordinates in all directions
    (cardinal + diagonal). Returns list of tuples. """
    height,width= _cell_coord
    N = (height -1, width)
    S = (height +1, width)
    W = (height , width - 1)
    E = (height , width + 1)
    NW = (height - 1 , width - 1)
    NE = (height - 1 , width + 1)
    SE = (height + 1 , width + 1)
    SW = (height + 1 , width - 1)
    return [W, SW, S, SE, E, NE, N, NW]


def populate_world(_world_size: tuple, _seed_pattern: str = None) -> dict:
    population_dict = {}
    if _seed_pattern is not None:
        my_pattern = cb.get_pattern( _seed_pattern, _world_size)
        print(my_pattern)

    height, width = _world_size

    for x in range(height):
        for y in range(width):
            coordinate =  (x, y)
            if x in [0,height-1] or y in [0,width-1]: #Check the outlying spaces
                population_dict[coordinate] = None
                continue
            if _seed_pattern is not None:
                if coordinate in my_pattern:
                    state = "X"
                else:
                    state = "-"
            else:
                ranNum = random.randrange(20) # as per PDF assignement
                if ranNum <= 16:
                    state = "X"
                else:
                    state = "-"

            value = {"state": state, "neighbours": calc_neighbour_positions(coordinate)}
            population_dict[coordinate] = value

    return population_dict

def count_alive_neighbours(_neighbours: list, _cells: dict) -> int:
    """ Determine how many of the neighbouring cells are currently alive. """
    living_counter=0
    for neighbor in _neighbours:
        if _cells[neighbor] is not None:
            if _cells[neighbor]["state"]=='X':
                living_counter+=1
    return living_counter

def update_world(_cur_gen: dict, _world_size: tuple) -> dict:
    """ Represents a tick in the simulation. """
    _next_gen={}
    _,max_width=_world_size
    for coordinates, values in _cur_gen.items():
        _,width=coordinates
        if values is not None:
            val=cb.get_print_value(values["state"])
            cb.progress(val)
            num_live_neighbors=count_alive_neighbours(values["neighbours"], _cur_gen)
            if num_live_neighbors==3 and values["state"]=="-":
                new_values={
                            "state":"X",
                            "neighbours": values["neighbours"]
                          }
            elif num_live_neighbors in (2,3) and values["state"]=="X":
                new_values={
                            "state":"X",
                            "neighbours": values["neighbours"]
                          }
            else:
                new_values={
                            "state":"-",
                            "neighbours": values["neighbours"]
                          }

            _next_gen[coordinates]=new_values
        else:
            val=cb.get_print_value("#")
            cb.progress(val)
            _next_gen[coordinates]=values
        if max_width-1==width:
            print("\n")
    return _next_gen

def run_simulation(_generations: int, _population: dict, _world_size: tuple):
    """ Runs simulation for specified amount of generations. """
    _gen=_population
    for gen in range(_generations):
        cb.clear_console()
        _gen=update_world(_gen, _world_size)
        sleep(0.2)

def main():
    """ The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!! """
    epilog = "DT179G Project v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('-g', '--generations', dest='generations', type=int, default=50,
                        help='Amount of generations the simulation should run. Defaults to 50.')
    parser.add_argument('-s', '--seed', dest='seed', type=str,
                        help='Starting seed. If omitted, a randomized seed will be used.')
    parser.add_argument('-ws', '--worldsize', dest='worldsize', type=str, default='80x40',
                        help='Size of the world, in terms of width and height. Defaults to 80x40.')
    parser.add_argument('-f', '--file', dest='file', type=str,
                        help='Load starting seed from file.')

    args = parser.parse_args()

    try:
        if not args.file:
            raise AssertionError
        population, world_size = load_seed_from_file(args.file)
    except (AssertionError, FileNotFoundError):
        world_size = parse_world_size_arg(args.worldsize)
        population = populate_world(world_size, args.seed)

    run_simulation(args.generations, population, world_size)


if __name__ == "__main__":
    main()
