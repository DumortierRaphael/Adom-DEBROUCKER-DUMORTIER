import random

def get_all_path():
    return [f'file/random{chr(i)}100.tsp' for i in range(65, 71)]


def get_letter_from_path(path) :
    return path[11:12]


def get_list_int_to_n(n) :
    points = [i for i in range(n)]
    random.shuffle(points)
    return points


def swap(points, i, j):
    points[i], points[j] = points[j], points[i]
    return points


def two_opt(points, i, j) :
    opti = points
    d = abs(j - i)
    d = (d + 1) / 2
    for k in range(d) :
        opti[i + k], opti[j - k] = points[j - k], points[i + k]
    return opti
