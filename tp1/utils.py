import random

def get_all_path():
    return [f'tp1/file/random{chr(i)}100.tsp' for i in range(65, 71)]


def get_letter_from_path(path) :
    return path[15:16]


def get_list_int_to_n(n) :
    points = [i for i in range(n)]
    random.shuffle(points)
    return points
