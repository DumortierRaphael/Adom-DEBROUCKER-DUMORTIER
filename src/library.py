from multiprocessing.dummy import current_process
import utils

#TP1
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
    if i < j :
        return matrix[i][j]
    else :
        return matrix[j][i]


def total_cost(matrix, points):
    len_list = len(points)
    total_cost = 0
    for i in range(len_list-1) :
        temp_cost = cost(matrix, points[i], points[i+1])
        total_cost += temp_cost
    total_cost += cost(matrix, points[0], points[-1])
    return total_cost, points


def cost_of_closest_point(matrix, points, main_point):
    all_total_cost = []
    for point in points[1:] :
        all_total_cost.append([point, cost(matrix, main_point, point)])
    min_point, min_cost = all_total_cost[0]
    for p in all_total_cost :
        p_min, p_cost = p
        if min_cost > p_cost:
            min_cost = p_cost
            min_point = p_min
    points.remove(min_point)
    points[0] = min_point
    return min_cost, points


def all_closest_point(matrix, dim) :
    points = utils.get_list_int_to_n(dim)
    closest_points = [points[0]]
    total_cost = 0
    while len(points) > 1 :
        closest_cost, points = cost_of_closest_point(matrix, points, points[0])
        total_cost += closest_cost
        closest_points.append(points[0])
    total_cost += cost(matrix, closest_points[0], closest_points[-1])
    return total_cost, closest_points


#TP2
def bestNeighborSwap(points, matrix):
    opti = points
    init_cost = total_cost(matrix, opti)
    best_cost = init_cost
    changes = 0
    best_gain = 0
    for i in range(len(points)) :
        for j in range(i+1, len(points)) :
            gain = gain_swap(i, j, points, matrix)
            if gain > best_gain:
                utils.swap(i, j, points)
                changes += 1;
                best_cost = init_cost - gain
                best_gain = gain
                opti = points
                utils.swap(i, j, points)
        if changes != 0 :
	        break
    if changes == 0 :
        return opti
    else :
        return bestNeighborSwap(opti, matrix)
            
