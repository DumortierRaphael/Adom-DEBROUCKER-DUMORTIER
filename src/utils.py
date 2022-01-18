import random

def get_all_path():
    return [f'file/random{chr(i)}100.tsp' for i in range(65, 71)]


def get_letter_from_path(path) :
    return path[11:12]


def get_list_int_to_n(n) :
    points = [i for i in range(n)]
    random.shuffle(points)
    return points


def get_two_randoms(points):
    length = len(points)
    r1, r2 = random.randrange(1, length), random.randrange(length)
    while r1 == r2:
        r2 = random.randrange(length)
    return r1, r2


def swap(points):
    r1, r2 = get_two_randoms(points)
    points[r1], points[r2] = points[r2], points[r1]
    return points


def two_opt(points):
    r1, r2 = get_two_randoms(points)
    if r1 > r2 :
        r1, r2 = r2, r1
    temp = points[r1:r2]
    temp.reverse()
    return points[0:r1] + temp + points[r2:]
