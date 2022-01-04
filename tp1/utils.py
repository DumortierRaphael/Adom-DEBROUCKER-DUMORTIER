import sys

def get_all_path():
    return [f'tp1/file/random{chr(i)}100.tsp' for i in range(65, 71)]

def get_letter_from_path(path) :
    return path[15:17]

def get_nb():
    n = 10
    if (len(sys.argv) > 1):
        n = int(sys.argv[1])
    return n
