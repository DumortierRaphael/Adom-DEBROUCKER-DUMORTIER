def get_path() :
    letter = str(input('Letter ? (A - F) : '))
    return f'tp1/file/random{letter.upper()}100.tsp'

def matrix(path) : 
    with open(path) as file:
        data = file.readlines()
    len_data = len(data)
    nb_lines = 3
    nb_iteration = 0
    matrix = []
    dim = int(data[nb_lines].split('DIMENSION :')[1].split('\n')[0])
    nb_lines += 4
    while nb_lines < len_data:
        temp = [0 for i in range(nb_iteration)]
        for i in range(dim-nb_iteration):
            line = data[nb_lines]
            temp.append(int(line))
            nb_lines += 1
        nb_iteration += 1
        matrix.append(temp)
    return matrix
