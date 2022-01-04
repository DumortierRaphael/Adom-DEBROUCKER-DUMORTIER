import random

def matrix_and_dim(path) : 
    with open(path) as file:
        data = file.readlines()
    len_data = len(data)
    nb_lines = 3
    nb_iteration = 0
    matrix = []
    dim = int(data[nb_lines].split('DIMENSION :')[1].split('\n')[0])
    nb_lines += 4
    while nb_lines < len_data:
        temp = [0 for _ in range(nb_iteration)]
        for _ in range(dim-nb_iteration):
            line = data[nb_lines]
            temp.append(int(line))
            nb_lines += 1
        nb_iteration += 1
        matrix.append(temp)
    return dim, matrix

def cost(matrix, i, j) :
    return matrix[i][j]

def total_cost(matrix, points) :
    len_list = len(points)
    total_cost = 0
    for i in range(len_list-1) :
        point_i = points[i]
        point_j = points[i+1]
        if point_i < point_j:
            temp_cost = cost(matrix, point_i, point_j)
        elif point_i > point_j:
            temp_cost = cost(matrix, point_j, point_i)
        else :
            temp_cost = 0
        total_cost += temp_cost
    return total_cost


def many_total_coast(nb_repeat, matrix, dim):
    all_total_cost = []
    points = [i for i in range(dim)]
    for _ in range(nb_repeat):
        random.shuffle(points)
        all_total_cost.append(total_cost(matrix, points))
    return all_total_cost
