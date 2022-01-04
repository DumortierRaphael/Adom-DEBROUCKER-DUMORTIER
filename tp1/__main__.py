import library
import utils

if __name__ == '__main__':
    all_path = utils.get_all_path()
    for path in all_path :
        letter = utils.get_letter_from_path(path)
        dim, matrix = library.matrix_and_dim(path)
        #2.3 | 3.1
        question2_3 = library.total_cost(matrix, dim)
        question3_1 = library.all_closest_point(matrix, dim)
        print(f'For {letter} |', question2_3, '|', question3_1)

