
def parse_world_size_arg(_arg: str) -> tuple: # Pick the grid size
    """ Parse width and height from command argument. """
    try:
        split_list = [int(item) for item in _arg.split("x")]
        if len(split_list) != 2:
            raise AssertionError("Wrong number of parameters")
        for value in split_list:
            #Check if below 1
            if value < 1:
                raise ValueError("Value is below 1")
        return tuple(split_list)
    except Exception as e:
        world_size = (80,40)
        return world_size


def populate_world(_world_size: tuple, _seed_pattern: str = None) -> dict:
    population_dict = {}
    my_pattern = cb.get_pattern( _seed_pattern, _world_size)
    print(my_pattern)
    height = _world_size[0]
    width = _world_size[1]



    for x in range(height):
        for y in range(width):
            coordinate =  (y, x)
            if x == 0 or x == 39 or y == 0 or y == 39:
                population_dict[coordinate] = None
            else:
                if _seed_pattern is not None:
                    if coordinate in my_pattern:
                        value = {"state": "X", "neighbours": calc_neighbour_positions(coordinate)}
                    else:
                        value = {"state": "-", "neighbours": calc_neighbour_positions(coordinate)}
                else:
                    ranNum = random.random()
                    if ranNum < 0.5:
                        value = {"state": "X", "neighbours": calc_neighbour_positions(coordinate)}
                    else:
                        value = {"state": "-", "neighbours": calc_neighbour_positions(coordinate)}


            population_dict[coordinate] = value

    return population_dict

def calc_neighbour_positions(_cell_coord: tuple) -> list:
    """ Calculate neighbouring cell coordinates in all directions (cardinal + diagonal).
    Returns list of tuples. """
    north_west = (_cell_coord[0] -1, _cell_coord[1] -1)
    for row in range(north_west[1], north_west[1]+3):
        for columns in range(north_west[0], north_west[0]+3)




    pass
